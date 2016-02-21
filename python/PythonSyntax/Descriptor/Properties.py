'''
Properties.py

A python implementation of the Property class

usage of Property

property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
'''


class Property(object):
    def __init__(self, fget = None, fset = None, fdel = None, doc = None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc

    def __get__(self, obj, objtype):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")
        return self.fget(obj)

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")
        self.fset(obj, value)

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        self.fdel(obj)

    def getter(self, fget):
        # type(self) get the type of the object, and with type(self)(...) create another instance of the same type as the object
        type(self)(fget, self.fset, self.fdel, self.__doc__)
# 
    def setter(self, fset):
        return type(self)(self.fget, fset, self.fdel, self.__doc__)
# 
    def deleter(self, fdel):
       return type(self)(self.fget, self.fset, fdel, self.__doc__)

class MyClass(object):
    def getx(self): return self.__x
    def setx(self, value): self.__x = value
    def delx(self): del self.__x
    x = Property(getx, setx, delx, "I'm the 'x' property")

c = MyClass()

c.x = 1
print c.x
del c.x
