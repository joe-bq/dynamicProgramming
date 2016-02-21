'''
Created on 2012-11-17

@author: Administrator
'''
from Classes.Inheritances.Shape import Shape

class Circle(Shape):
    '''
    classdocs
    '''
    def __init__(self, r = 1, x = 0, y = 0):
        '''
        Constructor
        '''
        super().__init__(x, y )
        self.radius = r