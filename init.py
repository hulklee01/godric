import http.server
from http import HTTPStatus
import json
import sqlite3


conn = sqlite3.connect("data.db")
c = conn.cursor()

class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_POST(self):

        data = self.rfile.peek()
        print(type(data))
        account = json.loads(data)
        print(type(account))

        uid = account['id']
        upw = account['password']

        c.execute('select password from users where id=?', (uid,))
        pw = c.fetchone()
        
        stat = 0
        content = {}

        if pw is not None and upw == pw[0]:
            stat = HTTPStatus.OK
            content = {'code':200}
        else:
            stat = HTTPStatus.NOT_FOUND
            content = {'code':404}

        self.send_response(stat)
        self.wfile.write(json.dumps(content).encode('UTF-8'))



if __name__ == "__main__":
    handler = RequestHandler
    server_address = ('',8000)

    httpd = http.server.HTTPServer(server_address, handler)
    print("WebServer Open")
    httpd.serve_forever()