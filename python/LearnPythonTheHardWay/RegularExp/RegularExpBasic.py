'''
Created on 2012-11-19

@author: Administrator

'''

import re

if __name__ == '__main__':
    regexp = re.compile("hello")
    count = 0
    file = open("textfile", 'r')
    for line in file.readlines():
        if regexp.search(line):
            count = count + 1
            file.close()
    print(count)