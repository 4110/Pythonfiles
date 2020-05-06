from wsgiref.simple_server import make_server
import json
import urllib

def api_app(environment, response):
    meth=environment['REQUEST_METHOD']
    if environment['PATH_INFO']== '/api':
        if meth=='POST':
            status = '201 Created'
            headers = [('Content-type', 'application/json; charset=utf-8')] 
            try:
                request_body_size = int(environment.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0

            request_body = environment['wsgi.input'].read(request_body_size)
            d = json.loads(request_body)

            deviceid = d['deviceid'] #to get the values parsed
            senval1 = d['senval1']
            lati = d['lati']
            longi = d['longi']
            uptime = d['uptime']
            devstatus = d['status']
          
            x={"Response":"Sucess","DeviceId":deviceid}
            x=json.dumps(x).encode('utf-8')
            response(status, headers)
            return [bytes(x)]

        elif meth=='GET':
            status = '200 OK'
            headers = [('Content-type', 'application/json; charset=utf-8')] 
            d = urllib.parse.parse_qs(environment['QUERY_STRING'])
            deviceid = d.get('deviceid', [''])[0]
            x={"Response":"Sucess","DeviceId":deviceid,"Latitude":"test","Longitude":"longi","Uptime":"now","Senval":"senvalnow","Status":"active"}
            x=json.dumps(x).encode('utf-8')
            response(status, headers)
            return [bytes(x)]
        elif meth=='PUT':
            status = '200 OK'
            headers = [('Content-type', 'application/json; charset=utf-8')] 
            try:
                request_body_size = int(environment.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0

            request_body = environment['wsgi.input'].read(request_body_size)
            d = json.loads(request_body)

            deviceid = d['deviceid'] #to get the values parsed
            senval1 = d['senval1']
            lati = d['lati']
            longi = d['longi']
            uptime = d['uptime']
            devstatus = d['status']

            x={"Response":"Sucess","Method":"Updated"}
            x=json.dumps(x).encode('utf-8')
            response(status, headers)
            return [bytes(x)]
        elif meth=='DELETE':
            status = '200 OK'
            headers = [('Content-type', 'application/json; charset=utf-8')] 
            d = urllib.parse.parse_qs(environment['QUERY_STRING'])
            deviceid = d.get('deviceid', [''])[0]
            x={"Response":"Sucess","DeviceId":deviceid,"Status":"Deleted"}
            x=json.dumps(x).encode('utf-8')
            response(status, headers)
            return [bytes(x)]
    else:   
        response('302 Found', [('Location', 'http://google.com')])
        return []  
server= make_server('',8000,api_app)
print("Started running at http:\\localhost:8000")
server.serve_forever()
