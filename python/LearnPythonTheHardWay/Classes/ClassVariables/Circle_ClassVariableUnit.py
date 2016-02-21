'''
Created on 2012-11-17

@author: Administrator
file: 
description:

'''
import unittest
from Classes.ClassVariables.Circle_ClassVariable import Circle

class Test(unittest.TestCase):


    def testClassVariable(self):
        c = Circle(3)
        print("*** size of c.area()")
        area = c.area()
        assert area == 3 * 3 * Circle.pi , "Test failed"
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testClassVariable']
    unittest.main()