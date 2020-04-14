#import picture from api
import json
from tkcalendar import DateEntry
import urllib.request
import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import datetime
root = tk.Tk()
def up():
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
        disimg.geometry("1400x1000")
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

        w =tk.Label(disimg, text=exp,height=7,width=150,wraplength=1200)
        w.pack()
        response = requests.get(img_url)
   
        img_data = response.content
        img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
        #tkinter print img
        disimg.title("APIIMAGE-Kise")
        panel = tk.Label(disimg, image=img)
        panel.pack(side="bottom", fill="both", expand="yes")
    else:
        print("Error")
        disimg.title("ERROR")
        w =tk.Label(disimg, text="Please select correct date.\n Date must be between Jun 16, 1995 to Today's Date.",height=3,width=100,wraplength=200)
        w.pack()
    disimg.mainloop()
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
