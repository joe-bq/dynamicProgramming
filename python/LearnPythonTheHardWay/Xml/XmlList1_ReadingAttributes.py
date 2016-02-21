'''
Created on 2012-4-23

@author: Administrator
'''

from xml.etree import ElementTree as ET


def main():
    element = ET.XML('<root><child val="One"/><child val="Two"/></root>')
    for subelement in element:
        print(subelement.attrib)

if __name__ == '__main__':
    main()
