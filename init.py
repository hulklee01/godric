import http.server
from http import HTTPStatus
import json
import sqlite3


conn = sqlite3.connect("data.db")
c = conn.cursor()

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):
        f = self.rfile.peek().decode()
        l = f.split('\"')
        uid = l[3]
        upw = l[7]
        
        c.execute('select password from users where id=?', (uid,))
        pw = c.fetchone()
        
        if pw is not None and upw == pw[0]:
            self.send_response(HTTPStatus.OK)
            content = '{\n\t\"code\":200\n}'
            body = content.encode('UTF-8')
            self.wfile.write(body)
        else:
            self.send_response(HTTPStatus.NOT_FOUND)
            content = '{\n\t\"code\":404\n}'
            body = content.encode('UTF-8')
            self.wfile.write(body)



if __name__ == "__main__":
    handler = RequestHandler
    server_address = ('',8000)

    httpd = http.server.HTTPServer(server_address, handler)
    print("WebServer Open")
    httpd.serve_forever()