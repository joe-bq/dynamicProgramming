'''
Created on 2012-11-8

@author: Administrator
file: PathOperation.py 
description: this file will demonstrate the use of path operations, such as the 
   os.path.join
   os.path.split
   os.path.splitext
   os.path.basename
   os.path.commonprefix
   os.path.expandvars
   os.path.isdir
   os.listdir
and constants
   os.pardir
   os.curdir
   os.path.exists
   os.path.isfile
      
'''

import os

def path_join():
    print(os.path.join('bin', 'utils', 'disktools'))
    
def path_split():
    print(os.path.split(os.path.join('some', 'directory', 'path')))

def path_basename():
    x = os.path.basename(os.path.join('some', 'directory', 'path.jpg'))
    print(x)
def path_dirname():
    x = os.path.dirname(os.path.join('some', 'directory', 'path.jpg'))
    print(x)

def path_common_prefix():
    path1 = os.path.join("some", "directory")
    path2 = os.path.join("some", "another_directory")
    x = os.path.commonprefix([path1, path2])    
    print(x)

def path_pardir():
    path = os.path.join(os.curdir, os.pardir, os.pardir)
    x = os.path.isdir(path)
    print(x)

def path_curdir():
    x = os.listdir(os.curdir)
    print(x)

def os_name():
    if os.name == 'posix':
        root_dir = '/'
    elif os.name == 'nt':
        root_dir = "C:\\"
    else:
        print("dont' understand this operating system")

def path_exists():
    x = os.path.exists('c:\\users\\Administrator\\umbrella0.txt')
    print("*** os.path.exists", x)    
def path_isfile():
    x = os.path.isfile('c:\\users\\Administrator\\umbrella0.txt')
    print("*** os.path.isfile", x)
        
if __name__ == '__main__':
    path_join()
    path_split()
    path_basename()
    path_common_prefix()
    path_pardir()
    path_curdir()
    os_name()