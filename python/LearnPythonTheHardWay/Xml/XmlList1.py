'''
Created on 2012-4-23

@author: Administrator
'''

from xml.etree import ElementTree as ET


def main():
    element = ET.XML(
       "<root><child>One</child><child>Two</child></root>")
    for subelement in element:
        print(subelement.text)

if __name__ == '__main__':
    main()

