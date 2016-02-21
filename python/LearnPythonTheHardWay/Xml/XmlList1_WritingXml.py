'''
Created on 2012-4-23

@author: Administrator
'''

from xml.etree import ElementTree as ET


def main():
    # create the root element
    root_element = ET.Element("root")
    # create the child <child>one</child>
    child = ET.SubElement(root_element, "child")
    # set the text of the child element, seems that the 
    # SubElement.text is a descriptor
    child.text = "One"
    
    # another way to do is to create 'Element' object and append that to the root
    child2 = ET.Element("child")
    child2.text = "Two"
    root_element.append(child2)
    
    # now inspect the value
    print(ET.tostring(root_element))

if __name__ == '__main__':
    main()