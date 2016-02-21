'''
Created on 2012-11-22

@author: Administrator
'''

from collections import UserList
class TypedUserList(UserList):
    '''
    classdocs
    '''
    def __init__(self, example_element, initial_list = []):
        '''
        Constructor
        '''
        super().__init__(initial_list)
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("second argument of TypeList must be a list")
        for element in initial_list:
            self.__check(element)
    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempt to add an element of incorrect type to a typed list.")
    def __setitem__(self, i, element):
        self.__check(element)
        self.data[i] = element
        pass
    def __getitem__(self, i):
        return self.data[i]
if __name__ == "__main__":
    x = TypedUserList("", 5 * [""])
    x[2] = "Hello"
    x[3] = "There"
    print(x[2] + " " + x[3])
    a,b,c,d,e = x # this works in a list context (it actually will retrieve the element one by one and assign to the variable to the left
    print(a, b, c, d)