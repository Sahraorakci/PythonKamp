from encodings import utf_8
from http.server import HTTPServer , BaseHTTPRequestHandler

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type" ,"text/html")
        self.end_headers()

        if(self.path=="/"):
            self.send_response(200)
            self.wfile.write(bytes("Hosgeldin <br>" , "utf8"))   
            self.wfile.write(bytes("Ilk istegin cevabidir.","utf8"))

        elif(self.path=="/baska"):
            self.send_response(200)
            self.wfile.write(bytes("Başka sayfaya hg <br>" , "utf8"))   
            self.wfile.write(bytes("Ilk istegin cevabidir.","utf8"))
        else:
            self.send_response(404)
            self.wfile.write(bytes("Sayfa bulunamadı", "utf8"))
    
    def yanitla (self , kod):
        self.send_response(kod)
        self.send_header("Content-type","text/html")
        self.end_headers()  
        
webserver = HTTPServer(("localhost" , 8000), MyServer )
try:
    webserver.serve_forever()
    print("Opened")
except KeyboardInterrupt:
    pass
webserver.server_close
print("Closed")