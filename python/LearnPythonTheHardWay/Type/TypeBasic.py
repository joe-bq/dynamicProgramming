'''
Created on 2012-11-21

@author: Administrator
'''

def type_basic():
    type_equal = type("hello") == type("Goodbye")
    type_equal = type(5)

def type_get_type():    
    class A:
        pass
    class B(A):
        pass
    b = B()
    type_info = type(b)
    type_info = b.__class__
    assert type_info == B, "b.__class__ != B"
    assert type_info == type(b), "b.__class__ == type(b)"

def type_isinstance():    
    class C:
        pass
    class D:
        pass
    class E(D):
        pass
    x = 12
    c = C()
    d = D()
    e = E()
    is_instance = isinstance(x, E) # false
    is_instance = isinstance(c, E) # false
    is_instance = isinstance(e, E) # true 
    is_instance = isinstance(e, D) # true
    is_instance = isinstance(d, E) # false

def type_issubclass():
    class C:
        pass
    class D:
        pass
    class E(D):
        pass
    issubclass(C, D)
    issubclass(E, D)
    issubclass(D, D)
    e = E()
    # remmber the type_get_type method? you can do the 
    # issubclass on the x.__class__
    issubclass(e.__class__, D)

if __name__ == '__main__':
    type_basic()
    type_get_type()
    type_isinstance()
    type_issubclass()