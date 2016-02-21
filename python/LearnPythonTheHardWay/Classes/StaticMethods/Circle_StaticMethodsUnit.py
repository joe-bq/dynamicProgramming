'''
Created on 2012-11-17

@author: Administrator
'''
import unittest
from Classes.StaticMethods.Circle_StaticMethods import Circle
import Classes.StaticMethods.Circle_StaticMethods as Circle2
from Classes.Circle_StaticMethods import Circle as Circle3

class Test(unittest.TestCase):


    def testTotal_area(self):
        c1 = Circle(1)
        c2 = Circle2.Circle(2)
        # c3 = Circle3(5)
        total_area = Circle.total_area() # you have to call Class.staticmethod for those method that has @staticmethod decorator
        assert total_area == 15.70795, "test failed!"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()