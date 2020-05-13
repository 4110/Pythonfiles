from wsgiref.simple_server import make_server
import json
import urllib
import mysql.connector
def api_app(environment, response):
    connection = mysql.connector.connect(host='localhost',
                                        database='raspidata',
                                        user='root',
                                        password='')
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
            print(deviceid)
            try:
                mySql_insert_query = """INSERT INTO datas (deviceid, status, uptime, longitude,latitude,senval) 
                                VALUES 
                                ('%s', '%s' , '%s' , '%s' , '%s' , '%s' )""" % (deviceid,devstatus,uptime,longi,lati,senval1)
                cursor = connection.cursor()
                cursor.execute(mySql_insert_query)
                connection.commit()
                cursor.close()
                x={"Response":"Sucess","DeviceId":deviceid,"Message":"Created"}
                x=json.dumps(x).encode('utf-8')
            except:
                x="error".encode('utf-8')
            response(status, headers)
            return [bytes(x)]

        elif meth=='GET':
            status = '200 OK'
            headers = [('Content-type', 'application/json; charset=utf-8')] 
            d = urllib.parse.parse_qs(environment['QUERY_STRING'])
            deviceid = d.get('deviceid', [''])[0]
            print(deviceid)
            try:
                mysql_select = """SELECT * FROM datas
                                WHERE deviceid='%s';""" % (deviceid)
                cursor = connection.cursor()
                cursor.execute(mysql_select)
                dat=cursor.fetchall()
                for n in dat:
                    dat=n
                x={"Response":"Sucess","DeviceId":dat[1],"Latitude": dat[5],"Longitude":dat[4],"Uptime":dat[3],"Senval":dat[6],"Status": dat[2]}
                x=json.dumps(x).encode('utf-8')
            except:
                x={"Response":"Specify Device ID"}
                x=json.dumps(x).encode('utf-8')
            cursor.close()
            connection.commit()
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
            try:
                request_body_size = int(environment.get('CONTENT_LENGTH', 0))
            except (ValueError):
                request_body_size = 0
            request_body = environment['wsgi.input'].read(request_body_size)
            d = json.loads(request_body)
            deviceid=d['deviceid']
            print(deviceid)
            mysql_delete = """DELETE FROM datas WHERE deviceid='%s'""" % (deviceid)
            cursor = connection.cursor()
            cursor.execute(mysql_delete)
            x={"Response":"Sucess","DeviceId":deviceid,"Status":"Deleted"}
            x=json.dumps(x).encode('utf-8')
            cursor.close()
            connection.commit()
            response(status, headers)
            return [bytes(x)]
    
    elif environment['PATH_INFO']=='/api/devices':
        status = '200 OK'
        headers = [('Content-type', 'application/json; charset=utf-8')] 
        mysql_select = """SELECT * FROM datas """
        cursor = connection.cursor()
        cursor.execute(mysql_select)
        dat=cursor.fetchall()
        js=[]
        for n in range(len(dat)):
            x={"Response":"Sucess","DeviceId":dat[n][1],"Latitude": dat[n][5],"Longitude":dat[n][4],"Uptime":dat[n][3],"Senval":dat[n][6],"Status": dat[n][2]}
            js.append(x)
        js=json.dumps(js).encode('utf-8')
        cursor.close()
        connection.close()
        response(status, headers)
        return [bytes(js)]
    else:
        status = '200 OK'
        headers = [('Content-type', '=/text/html; charset=utf-8')] 
        #response('302 Found', [('Location', 'http://google.com')])
        x="""<title>KiseAPI</title>
        <p>Send the request as url/api</p>"""
        x=x.encode('utf-8')
        response(status,headers)
        return [bytes(x)]  
server= make_server('',8000,api_app)
print("Started running at http:\\localhost:8000")
server.serve_forever()
