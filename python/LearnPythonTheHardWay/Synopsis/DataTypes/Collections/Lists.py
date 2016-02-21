'''
Created on 2012-10-22

@author: Administrator

file: Lists.py
description: this file is to test the use of the list - one of the built-in collection types s
'''

def demoLists():
    empty_list = []
    one_elem_list = [1]
    isovalent_list = [1, 2,3,4,5,6,7, 8, 9, 12]
    unisovalent_list = [1, "two", 3, 4.0, ["a", "b"], (5,6)] # 3L is no longer supported by python 3.x
    print("*** empty list ")
    print(empty_list)
    print("*** one element list ")
    print(one_elem_list)
    print("*** isovalent list ")
    print (isovalent_list)
    print("***unisovalent list")
    print(unisovalent_list)

def list_operation():
    x = [1, 2,3, 4, 5, 6, 7, 8, 9]
    print("*** original list:")
    print(x)
    print("*** len(x): ")
    print(len(x))
    y = [-1, 0] + x
    print("** print the concatenated list:")
    print(y)
    print("**reversed list")
    x.reverse() # you cannot do x = x.reverse(), otherwise, undefined behavior will happen
    print(x)
    x.remove(1)
    print(x)
    # another way of delete one element
    del x[1]
    print(x)
    
if __name__ == '__main__':
    demoLists()
    list_operation()