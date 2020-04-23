from wsgiref.simple_server import make_server
import json

def web_app(environment, response):
    c=environment['PATH_INFO']
    print(c)
    c=c.split("/")
    api='kise4110'
    print(c)
    if len(c)==3:
        d=c[2]
    else:
        d=c[0]
    if environment['PATH_INFO']== '/api/whoami/'+'api='+api: 
        status = '200 OK'
        headers = [('Content-type', 'application/json; charset=utf-8')]
        x={"Response":"Sucess","Name":"Kise", "Status":"Online",}
        x=json.dumps(x).encode('utf-8')
        response(status, headers)
        return [bytes(x)]
    elif environment['PATH_INFO']== '/api'+d or environment['PATH_INFO']== '/api/'+d:
        status = '200 OK'
        headers = [('Content-type', 'application/json; charset=utf-8')]
        x={"Response":"Error","Name":"None", "Status":"Offline","Request type":"/api/whoami/?api=yourapikey"}
        x=json.dumps(x).encode('utf-8')
        response(status, headers)
        return [bytes(x)]
    elif environment['PATH_INFO']== '/contact':
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        x=b'''
        <html>
        <title>Contact</title>
        <h1>Name:Kishore</h1>
        <h2>Mail:kishore4110@gmail.com</h2>
        <h3>Phone:+918682972636</h3>
        </html>
        '''
        response(status, headers)
        return [x]
    else:   
        response('302 Found', [('Location', 'http://google.com')])
        return []  

with make_server('',8000,web_app) as server:
    print("Started running at http:\\localhost:8000")
    server.serve_forever()
    
