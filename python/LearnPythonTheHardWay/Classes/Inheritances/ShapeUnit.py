'''
Created on 2012-11-17

@author: Administrator
'''
import unittest
from Classes.Inheritances.Shape import Shape
from Classes.Inheritances.Circle import Circle

class Test(unittest.TestCase):


    def testShape(self):
        c = Circle(r = 1, x = 0, y = 0)
        c.move(3, 4)
        assert 3 == c.x, "Test failed"
        assert 4 == c.y, "Test failed"

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testShape']
    unittest.main()