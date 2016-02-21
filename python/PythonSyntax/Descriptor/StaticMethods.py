'''
StaticMethods.py

Emumrate the creation of such Static methods in python
'''

class StaticMethod(object):
    "Emulate PyClassMehtod_Type() in objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, objtype=None):
        return self.f


'''A demo example'''
class E(object):
    def f(x):
        return x

    f = StaticMethod(f)

print E.f(3)
print E().f(3)
