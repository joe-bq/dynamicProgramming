'''
Created on 2012-11-17

@author: Administrator
'''
import unittest
from Classes.ClassMethods.Circle_ClassMethods import Circle

class Test(unittest.TestCase):


    def testClassMethods(self):
        c1 = Circle(1)
        c2 = Circle(2)
        Circle.total_area()
        c2.radius = 3
        Circle.total_area()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testClassMethods']
    unittest.main()