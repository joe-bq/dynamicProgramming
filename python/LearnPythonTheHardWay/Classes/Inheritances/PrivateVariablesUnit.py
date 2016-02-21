'''
Created on 2012-11-18

@author: Administrator
'''
import unittest
from Classes.Inheritances.PrivateVariables import Mine

class Test(unittest.TestCase):


    def testPrivateVariable(self):
        m = Mine()
        x = m.x
        with self.assertRaises(AttributeError):
            y = m.__y
            print("you shouldn't be able to see it")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()