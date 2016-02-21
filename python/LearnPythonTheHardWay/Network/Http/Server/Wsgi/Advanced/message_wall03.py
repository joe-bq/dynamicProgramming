'''
Created on 2012-11-27

@author: Administrator
file: message_wall03.py

'''

from wsgiref.simple_server import make_server
from io import StringIO
import sqlite3
import datetime


def get_form_vals(post_str):
    form_vals = {       item.split("=")[0]: item.split("=")[1] for item in post_str.decode().split("&")                 } # b'username=joe&usercount=1'
    return form_vals


def message_wall_app(environ, start_response):
    output = StringIO()
    status = b'200 OK'  # status OK 
    headers = [(b'Content-type', b'text/html; charset=utf-8')]
    start_response(status, headers)  # the status and response 
    
    print("<h1>Message Wall</h1>", file = output)
    
    if environ['REQUEST_METHOD'] == 'POST':
        size = int(environ['CONTENT_LENGTH'])
        post_str  = environ['wsgi.input'].read(size)
        form_vals = get_form_vals(post_str)
        form_vals['timestamp']= datetime.datetime.now()
        print(form_vals, "<p>", file = output)
        # cursor ?
        #
        cursor.execute("insert into messages (user, message, ts) values "
                       "(:user, :message, :timestamp)", form_vals)
    print('<form method="POST">User: <input type="text" '
            'name="user">Message: <input type="text" '
            'name="message"><input type="submit" value="Send"></form>',
            file=output)
    return [output.getvalue()]
        

httpd = make_server('', 8000, message_wall_app)
print("Serving on port 8000")

conn = sqlite3.connect("messagefile")
cursor = conn.cursor()

httpd.serve_forever()

