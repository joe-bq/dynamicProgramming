'''
Created on 2012-11-22

@author: Administrator
'''

class LineReader:
    def __init__(self, filename):
        self.fileobject = open(filename, 'r')
    # the key to be usable in the "for" method
    def __getitem__(self, index):
        line = self.fileobject.readline()
        if line == "":
            self.fileobject.close()
            raise IndexError # the for loop will depend on this IndexError to terminate the loop
        else:
            return line.split("::")[:2]


if __name__ == '__main__':
    # any object that defines __getitem__ as an instance method can return elements as if it 
    # were a list: all accesses of the form object[i] are transformed by Python into a mehtod 
    # invocation of the form object.__getitem__(i)
    for name, age in LineReader("data.txt"):
        print("name = {0:s}, age = {1:s}".format(name, age))