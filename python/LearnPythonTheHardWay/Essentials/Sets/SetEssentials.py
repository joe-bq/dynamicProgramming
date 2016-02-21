'''
Created on 2012-10-28

@author: Administrator
file: SetEssentials.py
description: SetEssentials.py demonstrate the 
   basic
       indice, len,  membreship, add, remove
    mutable set and the immutalbe/hashable frozenset
    set operators
       union, intersect, symmetric_difference
   
'''

def set_basics():
    x = set([1, 2, 3, 1, 3, 5])
    print("*** set has {} in representation")
    print(x)
    x.add(6)
    print(x)
    x.remove(5)
    print(x)
    y = 1 in x
    y = 4 in x
    print("*** set membership")
    print (y)
    
def set_ops():
    x = set([1, 2,3, 1, 3, 5])
    y = set([1, 7, 8, 9])
    union = x | y
    print("*** union")
    print(union)
    intersect = x & y
    print("*** intersect")
    print(intersect)
    symmetric_difference = x ^ y
    print("*** symmetric difference")
    print(symmetric_difference)


def frozenset_set():
    # set is not immmutable and hashaable
    # frozenset is like set but can't be changed after creation. Because frozensets immmutable and hdashble, they can be 
    # members of other sets
    x = set([1, 2, 3, 1, 3, 5])
    z = frozenset(x)
    print("*** frozenset - it has speical string representation")
    print(z)
        
if __name__ == '__main__':
    set_basics()
    set_ops()
    frozenset_set()