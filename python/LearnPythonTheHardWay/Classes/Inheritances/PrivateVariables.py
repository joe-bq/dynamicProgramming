'''
Created on 2012-11-18

@author: Administrator
'''

class Mine(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.x = 2
        self.__y = 3
    def print_y(self):
        print(self.__y)