'''
Created on 2012-11-17

@author: Administrator
'''
import unittest
from Classes.Circle import Circle

class Test(unittest.TestCase):


    def testRadius(self):
        c = Circle()
        c.radius = 3
        assert c.area() == 3 * 3 * 3.14159, "area failed!"
        
    def testRadius_Syntax2(self):
        c = Circle()
        c.radius = 3
        area = Circle.area(c)
        assert area == 3 * 3 * 3.14159, "area failed!"


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRadius']
    unittest.main()