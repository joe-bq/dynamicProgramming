'''
Created on 2012-11-24

@author: Administrator
'''
from collections import MutableSequence

class TypedList:
    def __init__(self, example_element, initial_list = []):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument of TypeList must be a list")
        for elem in initial_list:
            self.__check(elem)
        self.elements = initial_list[:]
    def __check(self, x):
        if not isinstance(x, self.type):
            raise TypeError("Attempt to add an element of incorrect type to a typed list")
    def __setitem__(self, i , element):
        self.elements[i] = element
    def __getitem__(self, i):
        return self.elements[i]

from abc import ABCMeta
class MyABC(metaclass = ABCMeta):
    pass


if __name__ == '__main__':
    from collections import MutableSequence
    is_sequence = issubclass(TypedList, MutableSequence)
    print("is_sequence is ", is_sequence)
    MutableSequence.register(TypedList)  # register a type to a base class will make the calling class the based class to the class in the parameter list
    is_sequence = issubclass(TypedList, MutableSequence)
    print("issubclass(TypedList, MutableSequence)", is_sequence)
    # ABC.register(list)
    MyABC.register(list)
    is_instance = isinstance([1,2,3], MyABC)
    print("is_instance is true", is_instance)

    