'''
Created on 2012-11-17

@author: Administrator
'''
from Classes.Inheritances import Shape
class Square(Shape):
    '''
    classdocs
    '''


    def __init__(self, side = 1, x = 0, y = 0): 
        '''
        Constructor
        '''
        # call the super (this is how you normally do the base sub-oject initialization)
        super().__init__(x, y)
        # super().__init__(x, y) # this is like the flexible way of calling the Shape.__init__(Shape, x, y)
        self.side =  side
