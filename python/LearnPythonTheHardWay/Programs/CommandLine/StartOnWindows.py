'''
Created on 2012-11-7

@author: Administrator
file: StartOnWindows.py 
description: This file - StartOnWindows.py is supposed to be used to demonstrate how to start a Python program on Windows Platform or in another sense, to make the 
   the python script directly executable on windows platform., however, the mian setup is not in the code itself, but rather how we create the short-cut and others. 
   Here is the code may have other use, e.g. shows you to use the getcwd - return the current executing directory 
'''
import sys, os
def main():
    print(os.getcwd())
    print(sys.argv)
    input("Hit return to exit")

import fileinput, glob, sys, os

def main2():
    '''On unix, you can do Python script.py sole*.tst > sole.data 
    while on windows, there is no wildcards expansion, so it will be passed in as it is "sole*.tst"
    you can leverage the glob.glob method as follow '''
    if os.name == 'nt':
        sys.argv[1:] = glob.glob(sys.argv[1])
    for line in fileinput.input():
        if not line.startswith('##'):
            print(line, end = " ")

if __name__ == '__main__':
    main()
    main2()