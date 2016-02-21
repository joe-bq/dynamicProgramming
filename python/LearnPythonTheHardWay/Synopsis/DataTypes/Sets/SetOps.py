'''
Created on 2012-10-22

@author: Administrator
file: SetOps.py
description: this file will demonstrate the use of set in Python
'''

def set_and_ops():
    x = set([1, 2, 3, 1, 3, 5])
    print ("*** set:")
    print(x)
    # the 'in' operator tells if an element exists in one set
    # think: what __getattr__ is needed in order to make the 'in' operator to work
    b = 1 in x
    print("*** in operator:")
    print(b)
    

if __name__ == '__main__':
    set_and_ops()