'''
Created on 2012-11-24

@author: Administrator
'''
from abc import ABCMeta, abstractmethod, abstractproperty
class MyABC(metaclass = ABCMeta):
    def __init__(self):
        self.__x = 0
    @abstractmethod
    def overrideme(self): 
        print("MyABC.overrideme()")
    @abstractproperty
    def readx(self):
        return self.__x
    def getx(self):
        return self.__x
    def setx(self, x):
        self.__x = x
    x = abstractproperty(getx, setx)
# create concrete class
class SecondABC(MyABC):
    def __init__(self):
        super().__init__()
        self.__x = 0
    def overrideme(self):
        super().overrideme() # it is common that you call the base classes's override method
        print("SecondABC.overrideme()")
    #@property
    def readx(self):
        return super().readx()
    def getx(self):
        return super().getx()
    def setx(self, x ):
        super().setx(x)
    x = property(getx, setx)
if __name__ == '__main__':
    try:
        my_abc = MyABC()
    except TypeError as e:
        pass
    my_secondAbc = SecondABC()
    my_secondAbc.overrideme()
    x = my_secondAbc.getx()
    print("*** ", x)