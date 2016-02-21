'''
Created on 2012-11-17

@author: Administrator
file: Circle.py
description: this is a basic class definition , which models Circle. 
'''

class Circle(object):
    '''
    Circle classes
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.radius = 1
    def area(self):
        return self.radius * self.radius * 3.14159
'''
1. Look for the method name in the instance namespace. If a method has been
changed or added for this instance, it¡¯s invoked in preference over methods in
the class or superclass. This is the same sort of lookup discussed later in section
15.4.1.

2 If the method isn¡¯t found in the instance namespace, look up the class type
class of instance, and look for the method there. In the previous examples,
class is Circle¡ªthe type of the instance c.

3 If the method still isn¡¯t found, look for the method in the superclasses.

4 When the method has been found, make a direct call to it as a normal Python,
using instance as the first argument of the function, and shifting all the other
arguments in the method invocation one space over to the right. So,
instance.method(arg1, arg2, . . .) becomes class.method(instance,
arg1, arg2, . . .).

'''