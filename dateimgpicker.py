#import picture from api
import json
import os
from tkcalendar import DateEntry
import urllib.request
import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import datetime
from functools import partial
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
root = tk.Tk()
c=""
def up():

    def email(url):
        kise=url
        mail=E2.get()
        E2.delete(0,'end')
        print(kise)
        part1="<html>"
        part2="<a href="+kise+"><img src="+kise+"></a>"
        part3="</html>"
        mail_content = part1+part2+part3

        #The mail addresses and password
        sender_address = 'care.deekshi@gmail.com'
        sender_pass = 'ur passsss'
        receiver_address = mail
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'API-Image'   #The subject line
        #The body and the attachments for the mail
        message.attach(MIMEText(mail_content, 'html'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

    #new window open from root window
    disimg=tk.Toplevel(root)
    c=cal.get()
    c=c.split("/")
    y=int(c[2]+c[0]+c[1])
    c=c[2]+"-"+c[0]+"-"+c[1]
    t=E1.get()
    print(t)
    t=t.split("/")
    t=int(t[2]+t[0]+t[1])
    print(y)
    if y>=19950615 and y<=t:
        disimg.geometry("1600x1000")
        print(c)
        # download raw json object
        url = "https://api.nasa.gov/planetary/apod?api_key=9sqsVN7tcAAMntHH8fhYcbzOrSK2KvdpKDfGal8d&date="+c
        data = urllib.request.urlopen(url).read().decode()
        #print(data)
        # parse json object
        obj = json.loads(data)
        # output some object attributes
        #print('$ ' + obj['hdurl'])--to print the decoded data
        #get the json object
        img_url = obj['url']
        exp=obj['explanation']
        hd_url =obj['hdurl']

        w =tk.Label(disimg, text=exp,height=6,width=250,wraplength=1500)
        w.config(font=("Courier", 9))
        w.grid()
        response = requests.get(img_url)
   
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        #tkinter print img
        disimg.title("APIIMAGE-Kise")
        panel = tk.Label(disimg, image=img)
        panel.grid()
        B = tk.Button(disimg, text ="Download",command=partial(download,img_url))
        B1 = tk.Button(disimg, text ="Download-HD",command=partial(download,hd_url))
        E2 = tk.Entry(disimg, bd =5)
        B2 = tk.Button(disimg, text ="Send Email",command=partial(email,img_url))
        B3 = tk.Button(disimg, text ="Set Wallpaper",command=partial(changewall,hd_url))
        B.place(x=140,y=100)
        B1.place(x=140,y=140)
        E2.place(x=140,y=180)
        B2.place(x=140,y=220)
        B3.place(x=140,y=260)
    else:
        print("Error")
        disimg.title("ERROR")
        w =tk.Label(disimg, text="Please select correct date.\n Date must be between Jun 16, 1995 to Today's Date.",height=3,width=100,wraplength=200)
        w.pack()
    disimg.mainloop()
def download(link):
    c=E1.get()
    c=c.split("/")
    c=c[2]+c[0]+c[1]
    r = requests.get(link, allow_redirects=True)
    name=c
    open(name+'.jpg', 'wb').write(r.content)
def changewall(url):
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+url)

root.title("Kise")
cal = DateEntry(root, width=12,date_pattern='mm/dd/y', background='darkblue', foreground='white', borderwidth=2)
t=cal.get()
w =tk.Label(root, text="Today's Date:",height=2,width=100,wraplength=200)
w.pack()
E1 = tk.Entry( bd =5,text=t)
E1.insert(0,t)
E1.configure(state='readonly')
E1.pack()
B = tk.Button(root, text ="Update", command = up)
cal.pack(padx=10, pady=10)
B.pack()
root.mainloop()
#coded by kise
