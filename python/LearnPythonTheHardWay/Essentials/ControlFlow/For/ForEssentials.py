'''
Created on 2012-11-1

@author: Administrator
file: ForEssentials.py
description: this file will demonstrate the use of for controls types
    range function
    tuple unpacking 
    enumerate 
    zip function
    list comprehension
    dictionary comprehension
    tuple comprehension - tuple generator
'''

def for_range():
    x = [1, 3, -7, 4, 9, -5, 4]
    for i in range(len(x)):
        if x[i] < 0:
            print("Fond a negate number at index ", i)
    range_x  = list(range(3, 7))
    print(range_x)

def for_loop_tuple_unpacking():
    print("*** for without unpack, tuple will be created")
    somelist = [(1, 2), (3, 7), (9, 5)]
    result = 0
    for t in somelist:
        result  = result + (t[0] * t[1])
    print("result = ", result)
    print("*** for loop with unpack")
    result = 0
    for x, y in somelist:
        result = result + (x * y)
    print("result = ", result)

def for_loop_enumerate():
    x = [1, 3, -7, 4, 9, -5, 4]
    for i, n in enumerate(x):
        if n < 0:
            print("Found a negative number at index ", i)    
def for_loop_zip():
    x = [1, 2, 3, 4]
    y = ['a', 'b', 'c']
    z = zip(x, y )
    list_z = list(z)
    print("*** zip will zip elements at the same position from two list")
    print(list_z)        

def list__dict_comprehension():
    print("*** for loop without list/dictionary comprehension")
    x = [1, 2, 3, 4]
    x_square = []
    for item in x:
        x_square.append(item * item)
    new_list = [item * item  for item in x if item > 2]
    # you may have the tuple comprehension, 
    # 
    print("*** for loop with list/dictionary comprehension")
    print(new_list)    
    x_square_dict = {item : item * item for item in x}
    print(x_square_dict)

def tuple_genreator():
    print("*** tuple comprehension")
    x = (1, 2, 3, 4)
    x_square = (item * item for item in x if item > 2)
    print(x_square)
    for item in x_square:
        print(item)
        
if __name__ == '__main__':
    for_range()
    for_loop_tuple_unpacking()
    for_loop_enumerate()
    for_loop_zip()
    list__dict_comprehension()
    tuple_genreator()