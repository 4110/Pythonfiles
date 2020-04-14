#import picture from api
import json
import urllib.request
import tkinter as tk
from PIL import ImageTk, Image
import requests
from io import BytesIO

# download raw json object
url = "https://api.nasa.gov/planetary/apod?api_key=9sqsVN7tcAAMntHH8fhYcbzOrSK2KvdpKDfGal8d"
data = urllib.request.urlopen(url).read().decode()
# parse json object
obj = json.loads(data)
# output some object attributes
#print('$ ' + obj['hdurl'])--to print the decoded data

root = tk.Tk()
img_url = obj['url']
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
#tkinter print img
root.title("Kise_api")
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="yes")
root.mainloop()
#coded by kise
