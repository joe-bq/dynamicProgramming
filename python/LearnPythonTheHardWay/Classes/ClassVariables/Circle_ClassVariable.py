'''
Created on 2012-11-17

@author: Administrator
file: Circle_ClassVariable
'''

class Circle(object):
    '''
    Circle classes
    '''
    pi = 3.14159
    def __init__(self, radius  = 1):
        '''
        Constructor
        '''
        self.radius = radius
    def area(self):
        return self.radius * self.radius * Circle.pi # you cannot do that with just 'pi'
