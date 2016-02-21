'''
Created on 2012-11-27

@author: Administrator
'''

from urllib.request import urlopen

url_file = urlopen("http://localhost:8000")
print(url_file.geturl())

print(url_file.info())


for line in url_file.readlines():
    print(line)
    
