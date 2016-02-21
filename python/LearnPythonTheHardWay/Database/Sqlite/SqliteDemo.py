'''
Created on 2012-11-26

@author: Administrator
'''


import sqlite3
conn = sqlite3.connect("datafile")

cursor = conn.cursor()
print(cursor)

cursor.execute("create table test (name text, count integer)") # create table
cursor.execute("insert into test (name, count) values ('Bob', 1)") # insert values 
cursor.execute("insert into test (name, count) values (?, ?)", ('Jill', 15)) #insert values 

cursor.execute("insert into test (name, count) values (:username, :usercount)", {"username": "Joe", "usercount": 10}) #insert values, with variable name prefixed with : in the query and pass in a corresponding dictionary

result = cursor.execute("select * from test")
print(result.fetchall())

result = cursor.execute("select * from test where name like :name", {"name" : "bob"})
print(result.fetchall())

cursor.execute("update test set count = ? where name = ?", (20, "Jill"))
result = cursor.execute("select * from test")
print(result.fetchall())


result = cursor.execute("select * from test")
for row in result:
    print(row)

cursor.execute("update test set count=? where name=?", (20, "Jill"))
conn.commit()
conn.close()    
