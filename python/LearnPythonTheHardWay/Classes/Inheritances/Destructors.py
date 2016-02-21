'''
Created on 2012-11-18

@author: Administrator
'''

class SpecialFiles(object):
    '''
    classdocs
    '''


    def __init__(self, file_name):
        '''
        Constructor
        '''
        self.__file = open(file_name, 'w')
        self.__file.write("**** Start Special File **** \n\n")
    def write(self, str):
        self.__file.write(str)
    def writelines(self, str_list):
        self.__file.writelines(str_list)
    def __del__(self):
        if self.__file is not None:
            print("__del__ called on", self.__file.name)
            self.__file.close()
        else:
            print("close() is already called")
    def close(self):
        if self.__file:
            self.__file.write('\n\n**** End Special File')
            self.__file.close()
            self.__file = None

class Circle:            
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.child = None
        if parent:
            parent.child = self
    def cleanup(self):
        self.child = self.parent = None
    def __del__(self):
        print("__del__ called on", self.name)
