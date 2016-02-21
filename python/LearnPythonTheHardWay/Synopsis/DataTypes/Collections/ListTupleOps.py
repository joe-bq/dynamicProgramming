'''
Created on 2012-10-22

@author: Administrator
file: ListTupleOps.py
description: this file demonstrate the conversion between list and tuples
'''
def convert_and_back():
    x = [1, 2, 3, 4]
    y = tuple(x)
    print ("*** list x:")
    print(x)
    print ("*** tuple x:")
    print(y)
    x = list(y)

if __name__ == '__main__':
    convert_and_back()