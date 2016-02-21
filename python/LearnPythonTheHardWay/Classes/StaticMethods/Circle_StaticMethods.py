'''
Created on 2012-11-17

@author: Administrator
file: 
description:  demonstrate the use/definition of the static method
 to define the static method, you will use the @staticmethod annotation

'''

class Circle(object):
    '''
    classdocs
    '''
    all_circles = []
    pi = 3.14159


    def __init__(self, r = 1):
        '''
        Constructor
        '''
        self.radius = r
        self.__class__.all_circles.append(self)
        
    def area(self):
        return self.__class__.pi * self.radius * self.radius
    
    # the key to t
    @staticmethod
    def total_area():
        total = 0
        for c in Circle.all_circles:
            total = total + c.area()
        return total