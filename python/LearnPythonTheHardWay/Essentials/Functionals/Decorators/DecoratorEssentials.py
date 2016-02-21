'''
Created on 2012-11-6

@author: Administrator
file: DecoratorEssentials.py
description: DecoratorEssentials.py is the file that demonstrate the use of decorator, a construct that help to decorate a function, and return a decorated function to the user.

it is the cuddle (chuxin) of functional programming, where you can compose a function by combining one or more functions with constants, or others. 
'''

def decorate(func):
    print("in decorate function, decorating", func.__name__)
    def wrapper_func(*args):
        print("Executing", func.__name__)
        return func(*args)
    return wrapper_func

def myfunction(parameter):
    print(parameter)

@decorate    
def myfunction2(parameter):
    print(parameter)    
    
if __name__ == '__main__':
    print("*** invoke decorate method directly")
    myfunction = decorate(myfunction)
    myfunction("hello")
    print("*** use of the decorate syntax @")
    myfunction2("Hello")
    