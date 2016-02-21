'''
Created on 2012-4-23

@author: Administrator
'''

class RoundFloat(float):
    '''
    This is the demo class to show that you can possibily create an subclass to the built-in types
        "__new__" is the method that exists to be overriden if you desired to inherit from base types 
    '''

#    def __init__(self):
#        '''
#        Constructor
#        '''
    def __init__(self, val):
        pass
#    def __new__(cls, val):
#        return super(RoundFloat, cls).__new__(cls, round(val, 2))
    def __new__(cls, val):
        return super(RoundFloat, cls).__new__(cls, round(val, 2))
#       the short-form is 
#       return super().__new__(cls, round(val, 2))

if __name__ == "__main__":
    roundFloat = RoundFloat(2.5)
    print(roundFloat)