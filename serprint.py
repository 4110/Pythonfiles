from escpos.printer import Serial
p = Serial(devfile='/dev/rfcomm0',
           baudrate=9600,
           bytesize=8,
           parity='N',
           stopbits=1,
           timeout=1.00,
           dsrdtr=True)
def printval(product,quantity,amount,billdate):
    p.set(align='right',text_type='B')
    p.text('            Unpluged\n')
    p.text("\n")
    p.text('Dt:'+billdate+'\n')
    p.text('Item: '+product+'\n')
    p.text("Quantitty: "+str(quantity)+"       "+'Price: '+str(amount)+"\n")
    #p.text('Thanks for using Unplugged')
