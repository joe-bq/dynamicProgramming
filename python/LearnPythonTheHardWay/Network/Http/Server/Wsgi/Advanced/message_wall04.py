'''
Created on 2012-11-27

@author: Administrator
'''

from wsgiref.simple_server import make_server
from io import StringIO
from urllib.parse import unquote_plus
import sqlite3
import datetime

def get_form_vals(post_str):
    form_vals = {       item.split("=")[0]: item.split("=")[1] for item in post_str.split("&")                 } # b'username=joe&usercount=1'
    return form_vals


def message_table(messages):
    table = "<table>\n"
    for message in messages:
        row_str = "<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>\n"
        table += row_str.format(message[2], message[0], message[1])
    table += "</table>"
    print('table generated is ', table)
    return table


def message_wall_app(environ, start_response):
    output = StringIO()
    status = b'200 OK'  # status OK 
    headers = [(b'Content-type', b'text/html; charset=utf-8')]
    start_response(status, headers)  # the status and response 
    
    print("<h1>Message Wall</h1>", file = output)
    
    if environ['REQUEST_METHOD'] == 'POST':
        size = int(environ['CONTENT_LENGTH'])
        post_str  = environ['wsgi.input'].read(size)
        post_str = unquote_plus(post_str.decode())
        print('decoded input is', post_str)
        form_vals = get_form_vals(post_str)
        form_vals['timestamp']= datetime.datetime.now()
        print(form_vals, "<p>", file = output)
        # cursor ?
        #
        cursor.execute("insert into messages (user, message, ts) values "
                       "(:user, :message, :timestamp)", form_vals)
    print("the PATH_INFO is ", environ['PATH_INFO'])
    path_vals = environ['PATH_INFO'][1:].split("/") #
    # 
    user, *tag = path_vals
    print ("user = ", user, "tags = ", *tag)
    cursor.execute("""select * from messages where user like ? or message
                    like ? order by ts""", (user, "@" + user + "%"))
    print(message_table(cursor.fetchall()), "<p>", file = output )
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
