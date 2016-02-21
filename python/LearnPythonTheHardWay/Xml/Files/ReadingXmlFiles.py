'''
Created on 2012-4-23

@author: Administrator
'''
import os
from xml.etree import ElementTree as ET


def main():
    xml_file = os.path.abspath(__file__)
    xml_file = os.path.dirname(xml_file)
    # a better way is to join the files
    # xml_file += '/our.xml'
    xml_file = os.path.join(xml_file, "our.xml")
    
    xml_file = r"C:\dev\workspace\PythonProject\Xml\Files\our.xml"
    
    
#    tree = ET.parse(xml_file)
#    if tree is not None:
#        it = tree.getiterator()
#        for i in it:
#            print(i)
    
    # better we wrap the parse code inside the necessary try-except code blocks
    try:
        tree = ET.parse(xml_file)
    # the old syntax is "except Exception, inst"
    # now it has been changed to the following in python 3.x
    except Exception as inst:
        print("Unexpected error opening %s: %s" % (xml_file, inst))
        pass
     
    
if __name__ == '__main__':
    main()


