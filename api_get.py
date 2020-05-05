# run in python 2
from wsgiref.simple_server import make_server
import json
from cgi import parse_qs, escape

def web_app(environment, response):
    c=environment['PATH_INFO'] 
    print(c)
    d = parse_qs(environment['QUERY_STRING'])
    deviceid = d.get('deviceid', [''])[0]
    senval1 = d.get('senval1',[''][0])
    senval2 = d.get('senval2',[''][0])
    status = d.get('status',[''][0])   
    uptime = d.get('uptime',[''][0])
    print(deviceid)
    print(senval1)
    print(senval2)
    print(status)
    print(uptime) 
    if environment['PATH_INFO']== '/api': 
        status = '200 OK'
        headers = [('Content-type', 'application/json; charset=utf-8')]
        x={"Response":"Sucess","Name":"Kise", "Status":"Online",}
        x=json.dumps(x).encode('utf-8')
        response(status, headers)
        return [bytes(x)]
    else:   
        response('302 Found', [('Location', 'http://google.com')])
        return []  

server=make_server('',8000,web_app)
print("Started running at http:\\localhost:8000")
server.serve_forever()
    
