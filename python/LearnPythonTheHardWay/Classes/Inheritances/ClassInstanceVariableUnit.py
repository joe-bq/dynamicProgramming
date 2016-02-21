'''
Created on 2012-11-18

@author: Administrator
'''
import unittest
import Classes.Inheritances.ClassInstanceVariable as C


class Test(unittest.TestCase):


    def testClassInstanceVariable(self):
        c = C.C()
        c.set_p()
        c.print_p()
        c.set_c()
        c.print_c()
        z = c.z
        z1 = C.C.z
        p = C.P.z
        assert z == z1, "Test failed"
        assert z1 == p, "Test failed"
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testClassInstanceVariable']
    unittest.main()