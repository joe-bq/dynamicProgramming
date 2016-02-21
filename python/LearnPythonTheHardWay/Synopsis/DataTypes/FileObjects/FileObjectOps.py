'''
Created on 2012-10-22

@author: Administrator
file: FileObjectOps.py 
description: this file will demonstrate the use of FileObject 
'''
def fileobject_ops():
    # open, write and close
    f = open("myfile", "w")
    f.write("first line with necessary newline character\n")
    f.write("Second line to write to the file\n")
    f.close()
    
    # open, read and close
    f = open("myfile", "r")
    line1 = f.readline()
    line2 = f.readline()
    f.close()
    print(line1, line2)
    
    import os
    print(os.getcwd())
    os.chdir(os.path.join("c:\\", "Users", "Administrator", "Documents", "Pictures"))  # os.path.join("c:", "Users") do not work os.path.join("c:\", "Users")
    filename = os.path.join("c:\\", "Users", "Administrator", "Documents", "test", "myfile") # 
    print(filename)
    
    f = open(filename, "r")
    print(f.readline())
    
    f.close()

if __name__ == '__main__':
    fileobject_ops()