'''
Created on 2012-11-22

@author: Administrator
file: SpecialMethodBasic.py
description: SpecialMethodBasic.py demonstrate some common special method, in this example,we are going to examine the method __str__ which can convert an object to user-readable strings
'''


class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue
    def __str__(self):
        return "Color: R={0:d}, G={1:d}, B={2:d}".format(self._red, self._green, self._blue)

if __name__ == '__main__':
    c = Color(15, 35, 3)
    print("*** ", str(c))
    assert str(c) == "Color: R=15, G=35, B=3", "__str__ method wrong!"
