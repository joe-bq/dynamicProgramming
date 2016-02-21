'''
Created on 2012-11-18

@author: Administrator
'''
import unittest
from Classes.Inheritances.Destructors import SpecialFiles
from Classes.Inheritances.Destructors import Circle


class Test(unittest.TestCase):


    def testDestructors(self):
        f = SpecialFiles('testfile')
        f.write('11111\n')
        f.close() 
    def testDestructors1(self):
        f = SpecialFiles('testfile')
    
    def testMemoryLeakage(self):
        # you won't see
        #  __del__ called on
        a = Circle("a", None)
        b = Circle("b", a)
        
    def testToBreakCircularReferences(self):
        c = Circle('c', None)
        d = Circle('d', c)
        d.cleanup()
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testDestructors']
    unittest.main()