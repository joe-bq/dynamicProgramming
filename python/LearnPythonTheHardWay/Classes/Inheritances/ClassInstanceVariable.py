'''
Created on 2012-11-18

@author: Administrator
'''

class P:
    z= "Hello"
    def set_p(self):
        self.x = "Class P"
    def print_p(self):
        print(self.x)
class C(P):
    def set_c(self):
        self.x ="Class C"
    def print_c(self):
        print(self.x)
        