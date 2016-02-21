'''
Created on 2012-10-28

@author: Administrator
file: PythonEssentials.py
description: TupeEssentials.py demonstrate the 
   basic
       indice, min, max, len, membreship
   tuple being immutable
   concat +
   initialize *
   copy
   one element tuple
   pack and unpack tuples
   pack and unpack in general
   convert list and tuple
   string related special tuple and list op
   convert tuple and list 
   
'''

def tuple_basic():
    x = ('a', 'b', 'c')
    y = x[2]
    print("*** tuple index")
    print(y)
    y = x[1:]
    print("*** tuple slice")
    print(y)
    y = len(x)
    print("*** len")
    print(y)
    y = max(x)
    print("*** max")
    print(y)
    y = min(x)
    print("*** min")
    print(y)
    y = 5 in x
    print("*** membeship in tuple : 5 in x")
    print(y)
    y = 5 not in x
    print("*** membership in tuple : 5 not in x")
    print(y)

def tuple_can_not_modify():
    try:
        x = (1, 2, 3, 4)
        x[2] = 'd'
    except TypeError:
        print("tuple can not modify")
        
def tuple_concat():
    x = ('a', 'b', 'c')
    y = x + x
    print("*** (tuple) + (tuple)")
    print(y)

def tuple_initialize():
    x = ('a', 'b', 'c')
    y = x * 2
    print("*** (tuple) * 2")
    print(y)
    y = 2 * x      
    print("*** 2 * (tuple)")
    print(y)    

def tuple_copy():
    x = ('a', 'b', 'c')
    print("*** copy ")
    y = x[:]
    print(y)
    print("*** other ways of copy : y = x * 1; y = x + ()")
    y =  x * 1
    y = x + () 
    import copy
    y = copy.deepcopy(x)
    print("*** deep copy on tuple")
    print(x)

def one_element_tuple():
    x = 3
    y = 4
    z = (x + y,)
    print("*** one element tuple")
    print(z)
    print("*** the output is special treated for one element tuple")

def pack_unpack_tuple():
    (one, two, three, four) = (1, 2, 3, 4)
    print ("*** tuple in assignment context ")
    print("*** tuple unpack: one = ", one)
    one, two, three, four = 1, 2, 3, 4
    print("*** tuple unpack in simplified syntax")
    print("*** the tuple unpack: one = ", one)
    print("*** tuple help swaps ")
    one, two = two, one
    print("*** extended unpack feature")
    x = (1, 2, 3, 4)
    a, b, *c  = x
    print((a, b, c))
    *a, b, c = x
    print((a, b, c))
    a, b, c, d, *e, = x
    print((a, b, c, d, e))
    print("*** starred element receives all the surplus items as a list, if no surplus elements, it receives an empty list")

def pack_unpack_general():
    [a, b] = [1, 2]
    [c, d] = 3, 4
    [e, f] = (5, 6)
    (g, h) = 7, 8 
    i, j = [9, 10]
    k, l = (11, 12)
    
def convert_list_tuple():
    x = list((1, 2, 3, 4))
    print(x)
    x = tuple([1, 2, 3, 4])
    print(x)

def string_special_tuple_list():
    y = list("hello")
    print(y)
    x = tuple("hello")
    print(x)    
    
if __name__ == '__main__':
    tuple_basic()
    tuple_can_not_modify()
    tuple_concat()
    tuple_initialize()
    tuple_copy()
    one_element_tuple()
    pack_unpack_general()
    convert_list_tuple()
    string_special_tuple_list()
