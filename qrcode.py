# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import time
import requests
from escpos.printer import *
import serial

print("[INFO] starting video stream...")
vs = VideoStream(src=0,usePiCamera=False).start()
time.sleep(2.0)
URL = 'http://127.0.0.1:5000/billprint'
# open the output CSV file for writing and initialize the set of
# barcodes found thus far
while True:
    frame = vs.read()
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcodeData = barcode.data.decode('utf-8')
        barcodeType = barcode.type
        print(barcodeData)
        param = {'ordernumber':barcodeData,'deviceid':123456}
        r = requests.get(url = URL,params = param)
        print(r.json())
        if r.json.get('msg',None)=='success':
            p = Serial(devfile='/dev/rfcomm0',
                       baudrate=9600,
                       bytesize=8,
                       parity='N',
                       stopbits=1,
                       timeout=1.00,
                       dsrdtr=True)
            p.set(align='right',text_type='B')
            p.text("            Unpluged\n")
            p.text("\n")
            p.text("Order Num:"+barcodeData+"\n")
            p.text('Date: k\n')
            p.text('Name: Quantitty\n')
            p.text('Thanks for using Unplugged!')
            p.cut()
        else:
            print('error')
        time.sleep(5)
