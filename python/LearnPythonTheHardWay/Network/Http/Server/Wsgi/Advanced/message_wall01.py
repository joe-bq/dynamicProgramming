'''
Created on 2012-11-27

@author: Administrator
file: message_wall01.py

'''

from wsgiref.simple_server import make_server

def message_wall_app(environ, start_response):
    status = b'200 OK'  # status OK 
    headers = [(b'Content-type', b'text/html; charset=utf-8')]
    start_response(status, headers)  # the status and response 
    
    return ["<h1>Message wall</h1>"] # why it it the list that is returned?


httpd = make_server('', 8000, message_wall_app)
print("Serving on port 8000 ....")
httpd.serve_forever()