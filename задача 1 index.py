from http.server import HTTPServer, CGIHTTPRequestHandler
 
 
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()

print("Content-type: text/html; charset=utf-8")
print()
print("<h1>Привет, Яндекс! Я - я</h1>")