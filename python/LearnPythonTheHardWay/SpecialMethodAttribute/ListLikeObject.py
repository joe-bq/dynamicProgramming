'''
Created on 2012-11-22

@author: Administrator
'''

if __name__ == '__main__':
    fileobject = open("StrMethod.py", "r")
    lines = fileobject.readlines()
    fileobject.close()
    for line in lines:
        print(line)
    
    # you can treat the fileobject as lines of text 
    fileobject = open("StrMethod.py", "r")
    for line in fileobject:
        print(line)
