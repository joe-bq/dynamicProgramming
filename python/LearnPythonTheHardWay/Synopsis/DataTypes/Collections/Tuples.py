'''
Created on 2012-10-22

@author: Administrator
file: Tuples.py
description: this module file demonstrate how to use the tuples
'''

def define_tuples():
    empty_tuple = ()
    one_element_tuple = (1,) # think why we must have (1,) rather than (1)
    isovalent_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 12)
    nonisovalent_tuple = (1, "two", 3, 4.0, ["a", "b"], (5, 6)) # it is not allowed to have 3L in python 3.x now

    print("*** empty tuple\n", empty_tuple)
    print("*** one element tuple\n", one_element_tuple)
    print("*** isovalent tuple\n", isovalent_tuple)
    print("*** nonisovalent_tuple\n", nonisovalent_tuple)

if __name__ == '__main__':
    define_tuples()