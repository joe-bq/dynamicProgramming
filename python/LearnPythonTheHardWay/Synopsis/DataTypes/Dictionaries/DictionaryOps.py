'''
Created on 2012-10-23

@author: Administrator
file: DictionaryOps.py
description: this file will demonstrate the use of Dictionaries in Python
'''
def dictionary_ops():
    x = {1: "one", 2: "two"}
    x['first']  = "one"
    x[("Delorme", "Ryan", 1995)] = (1, 2, 3)  # tuple can be the dictionary key and tuple can be the dictionary value , Keys must be of immutable types
    print("*** the dictionary")
    print(x)
    print("*** value to key 1")
    print(x[1])
    print("*** dictionary.get accepts default value")
    print(x.get(1, "not available"))
    del x[1]
    print ("*** after delete 1, the dictionary ")
    print(x)

if __name__ == '__main__':
    dictionary_ops()