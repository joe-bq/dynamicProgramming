'''
Created on 2012-11-18

@author: Administrator
file: Properties.py
description: this file will demonstrate the use of the @property and the @.setter decorator
'''

class Temperature(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._temp_fahr = 0
    @property
    def temp(self):
        return (self._temp_fahr - 32) * 5 / 9

    # what if you want to define a setter property
    @temp.setter
    def temp(self, new_temp):
        self._temp_fahr = new_temp * 9 / 5 + 32