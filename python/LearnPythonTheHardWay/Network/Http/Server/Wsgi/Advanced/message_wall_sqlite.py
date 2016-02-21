'''
Created on 2012-11-27

@author: Administrator
'''

import sqlite3

conn = sqlite3.connect("messagefile", \
                       detect_types = sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cursor = conn.cursor()
cursor.execute("create table messages (user text, message text, ts timestamp)")
conn.commit()
conn.close()
