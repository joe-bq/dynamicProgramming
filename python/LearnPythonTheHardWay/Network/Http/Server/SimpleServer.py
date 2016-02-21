'''
Created on 2012-11-27

@author: Administrator
'''

from http.server import  HTTPServer, SimpleHTTPRequestHandler


server =  HTTPServer(("", 8000), SimpleHTTPRequestHandler) # the ("", 8000) define the address and port for the server

server.serve_forever() # this is like the forever loop 

if __name__ == '__main__':
    pass