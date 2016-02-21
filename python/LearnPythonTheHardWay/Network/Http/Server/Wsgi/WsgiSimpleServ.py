'''
Created on 2012-11-27

@author: Administrator
'''

from wsgiref.simple_server import make_server

def hello_world_app(environ, start_response): # this is the wsgi reponse handler
    status = b'200 OK'  # status OK 
    headers = [(b'Content-type', b'text/plain; charset=utf-8')]
    start_response(status, headers)  # the status and reponse 
    return [b"Hello World"]          # followed by the contnet "hello world"

httpd = make_server('', 8000, hello_world_app) # make_server:make_server , passing in the application object , and the address and port for the server
print("Serving on port 8000...")

httpd.serve_forever() # start up the servers, you can make it serve only once by using handle_request:handle_one
