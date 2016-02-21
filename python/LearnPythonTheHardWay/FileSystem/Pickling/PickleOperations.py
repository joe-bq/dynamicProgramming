'''
Created on 2012-11-12

@author: Administrator
file: PickleOperation.py
description: this file will demonstrate the use of the the pickle module 
pickling is the major benefit in python, use this ability
'''

import pickle

def pickle_common():
    # it used to work in the  pyton 2.x version : http://docs.python.org/2/howto/unicode.html
    # path = u"state" 
    # always remember to open the file with the same encoding or binary mode, otherwise, the pickle module won't work propperly
    # file = open("state".encode('utf-8'), 'wb')
    file = open("state", 'wb')
    a = "string"
    b = 1
    c  = (1.0, 2.0)
    data = {'a': a, 'b': b, 'c': c}
    pickle.dump(data, file)
    file.close()
    # restore the pickled data
#    file = open("state", 'rb')
    file = open('state', 'rb')
    data = pickle.load(file)
    file.close()
    print("*** after pickling...")
    print(data)
    
    
if __name__ == '__main__':
    pickle_common()