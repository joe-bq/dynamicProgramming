'''
Created on Oct 17, 2013

@author: wangboqi

REMARKS: in python, you will never find yourself in need of a multiple constructor, if you ever find yourself in such a situation, doubt  your design first.

Here is presented just for your interest. 


BUG: this node is not complete through, and it still has errors. For one, how do you iterator through the collection?

REFERENCES:
Multiple constructors in a Python class: http://pythonconquerstheuniverse.wordpress.com/2010/03/17/multiple-constructors-in-a-python-class/
'''

import pprint

class Vector:
    """
    Demo of a class with multiple signature for the constructor 
    """
    def __init__(self, first=[], *rest, **kwargs):
        if rest:
            self.values = [first]
        else:
            self.values = []
            rest = first;
        self.values.extend(rest)
        
#         if __debug__:
#             pprint.pprint(self, self.values)
            #print self.values
        
    def __iter__(self):
        for item in self.values:
            yield item

#         def next(self):
#             self.i += 1
#             if self.i == 3:
#                 raise StopIteration
#             else:
#                 return self.i
            
                
if __name__ == "__main__":
    #v = Vector()
    v = Vector(1, 2, 3)
    for a in v:
        print a
    v = Vector([4, 5, 6])
    for a in v:
        print a
    #q = Vector(v);
    #r = Vector(v, [v], v)