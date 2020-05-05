from wsgiref.simple_server import make_server
import json
from cgi import parse_qs, escape

def api_app(environment, response):
    meth=environment['REQUEST_METHOD']
    if environment['PATH_INFO']== '/api':
        status = '200 OK'
        headers = [('Content-type', 'application/json; charset=utf-8')] 
        if meth=='POST':
            print("booooooooo")
            try:
                request_body_size = int(environment.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0

            # When the method is POST the variable will be sent
            # in the HTTP request body which is passed by the WSGI server
            # in the file like wsgi.input environment variable.
            request_body = environment['wsgi.input'].read(request_body_size)
            d = json.loads(request_body)

            deviceid = d['deviceid'] #to get the values parsed
            senval1 = d['senval1']
            lati = d['lati']
            longi = d['longi']
            uptime = d['uptime']
            devstatus = d['status']
            print(deviceid)
            print(uptime)
            #for escape to prevent injecto
            print(deviceid)
            x={"Response":"Sucess","DeviceId":deviceid}
            x=json.dumps(x).encode('utf-8')
            response(status, headers)
            return [bytes(x)]

        elif meth=='GET':
            d = parse_qs(environment['QUERY_STRING'])
            deviceid = d.get('deviceid', [''])[0]
            x={"Response":"Sucess","DeviceId":deviceid,"Latitude":"test","Longitude":"longi","Uptime":"now","Senval":"senvalnow","Status":"active"}
            x=json.dumps(x).encode('utf-8')
            response(status, headers)
            return [bytes(x)]
    else:   
        response('302 Found', [('Location', 'http://google.com')])
        return []  
server= make_server('',8000,api_app)
print("Started running at http:\\localhost:8000")
server.serve_forever()
