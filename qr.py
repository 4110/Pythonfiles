# import the necessary packages
from imutils.video import VideoStream
from pyzbar import pyzbar
import time
import requests
from serprint import printval

print("[INFO] starting video stream...")
vs = VideoStream(src=0,usePiCamera=False).start()
time.sleep(2.0)
URL = 'http://192.168.43.21:5000/billprint'
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
        r=r.json()
        dat=r['msg']
        print(dat)
        if dat=='success':
            product= r['product']
            quantity = r['quantity']
            amount= r['amount']
            datebilled= r['date']
            printval(product,quantity,amount,datebilled)
        else:
            print('error')
        time.sleep(5)
