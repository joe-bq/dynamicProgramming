'''
Created on 2012-11-17

@author: Administrator
'''

class Shape:
    '''
    classdocs
    '''
    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
    
    def move(self, delta_x, delta_y):
        self.x = self.x + delta_x
        self.y = self.y + delta_y