'''
Created on 2012-11-23

@author: Administrator
'''

class Spam:
    '''
    classdocs
    '''
    def __init__(self, x):
        '''
        Constructor
        '''
        self.x = x
    def show(self):
        print(self.x)

if __name__ == "__main__":
    # create the object
    my_spam = Spam("test")
    # <class '__main__.Spam'
    t = type(my_spam)
    print("*** ", t)
    # <class 'type'>
    t = type(Spam)
    # test
    print("*** ", t)
    my_spam.show()