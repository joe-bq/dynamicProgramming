'''
Created on 2012-11-17

@author: Administrator
file: Circle_ClassMethods.py
description: the benefit of the ClassMethod over the StaticMethod is that ClassMehtod will be implicitly passed in the class that they belongs to, so that subclass of Circle can still call total_area and refer to their own members

the signature of the classmethod is like this
    def class_method(cls):
the signature of the staticmethod is like this
    def static_method(): 
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
    
    @classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total