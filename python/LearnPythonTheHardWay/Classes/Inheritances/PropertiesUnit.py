'''
Created on 2012-11-18

@author: Administrator
'''
import unittest
from Classes.Inheritances.Properties import Temperature

class Test(unittest.TestCase):

    def testProperties(self):
        t = Temperature()
        self.assertEqual(t._temp_fahr, 0, "Test failed")
        self.assertEqual(t.temp, -17.777777777777779, "Test failed")
        t.temp = 34
        self.assertEqual(t._temp_fahr, 93.200000000000003, "Test failed")
        self.assertEqual(t.temp, 34.0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testProperties']
    unittest.main()