'''
StaticMethods.py

Emumrate the creation of such ClassMethod in python
'''

class ClassMethod(object):
    "Emulate PyClassMehtod_Type() in objects/funcobject.c"

    def __init__(self, f):
        self.f = f

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)
        def newfunc(*args):
            return self.f(klass, *args)
        return newfunc


'''A demo implementation of the Dict.fromkeys method, which is a class factory method that create Dictionary'''

class Dict(object):
    '''...'''
    def fromkeys(klass, iterable, value = None):
        "Emulate dict_fromkeys() in Objects/dictobject.c"
        d = klass()
        for key in iterable:
            # without the __getitem__, __setitem__, __delitem__, do this
            #d.__dict__[key] = value
            d[key] = value
        return d
    # check on "Python: implemnet list-like index access
    # from  http://stackoverflow.com/questions/6486387/python-implement-list-like-index-access
    def __getitem__(self, key):
        self.__getattribute__(key)

    def __setitem__(self, key, value):
        self.__setattr__(key, value)

    def __delitem__(self, key):
        self.__delattr__(key)
    
    fromkeys = ClassMethod(fromkeys)

dictionary = Dict.fromkeys(['h','e','l','l','o'])

# without the __getitem__, __setitem__, __delitem__, do this
#print dictionary.__dict__

print dictionary

class E(object):
    def f(klass, x):
        return klass.__name__, x

    f = ClassMethod(f)

print E.f(3)
print E().f(3)
