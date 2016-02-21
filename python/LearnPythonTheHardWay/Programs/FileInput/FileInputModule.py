'''
Created on 2012-11-7

@author: Administrator
file: FileInputModule.py
description: FileInputModule.py helps to demonstrate the use of fileinput module, the fileinput module support processing lines of input from one or more files.
'''
import fileinput
def main():
    for line in fileinput.input():
        if not line.startswith("#"):
            print(line, end = " ")
            


if __name__ == '__main__':
    print('we are going to examine the content of ... .... ')
    main()
    
# to test the program, you can run with the following input line.
#> python FileInputModule.py txt1.tst txt2.tst

