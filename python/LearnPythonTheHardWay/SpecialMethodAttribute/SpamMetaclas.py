'''
Created on 2012-11-23

@author: Administrator
'''

def init(self, x):
    self.x = x
def show(self):
    print(self.x)
# with the type class, you can create a type on the fly, where you can specify the
#   name
#   base classes
#   method list
# to that new type created
#  
Spam = type("Spam", (object,), {'__init__': init, 'show' : show})
def test_metaclass():
    class NewType(type):
        def __init__(cls, name, bases, dict):
            print("Create from newType")
            # super().__init__(cls, name, bases, dict)
            type.__init__(cls, name, bases, dict)
            cls.new_attr = "test"

    class Spam(metaclass = NewType):
        def __init__(self, x):
            self.x=x
        def show(self):
            print(self.x) # you will see the attribute from the parent 
    # you will see the meta-class be initialized 
    #  'Create from newType'
    # 
    print("", Spam.new_attr)
    print("type(Spam)", type(Spam)) # it will show NewType rather than type (normally if you don't override the metaclass, the result returned is 'type' 
    my_spam = Spam("Test")          # 
    print("type(my_spam)", type(my_spam)) # it will show __main__.Spam (just as any other variable will be  
    my_spam.show()
if __name__ == "__main__":
    my_spam = Spam("test")
    t = type(my_spam)
    print("*** ", t)
    t = type(Spam)
    print("*** ", t)
    my_spam.show()
    test_metaclass() # settle down on the test_metaclasses