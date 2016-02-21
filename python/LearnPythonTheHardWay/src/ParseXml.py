'''
Created on 2012-4-23

@author: Administrator
'''

from xml.etree import ElementTree as ET


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    

def main():
    element = ET.XML("<root><child>One</child><child>Two</child></root>")
    for subelement in element:
        print(subelement.text)
    print("this is the first python code that I've written")
    
    
if __name__ == "__main__":
    main()    