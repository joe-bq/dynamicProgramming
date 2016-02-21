'''
Created on 2012-11-9

@author: Administrator
file: FileOperations.py
description: this file will be used to demonstrate the file operations, this will include the following. 
   open 
   file modes
   write 
   close
   binary and text files
   with statement to guard against the file operation
'''

import sys

def file_open():
    file_object = open('FileOperations.py', 'r')
    line = file_object.readline()
    file_object.close()

def file_deterministic_cleanup():
    '''there is a discussion on the http://stackoverflow.com/questions/5071121/raii-in-python-automatic-destruction-when-leaving-a-scope
    the topic is 
       Is RAII (Resource Allocation is initialization)
    while the conclusion from delnan is 
       There can't be stack-based cleanup in a language using GC
       Deterministic cleanup happens through the with statement. 
       Python has a scope per function, class, and module. Period.
    also, check out the blog here: 
       http://www.cnblogs.com/bettermanlu/archive/2011/09/20/2182645.html
    '''
    with open('FileOperations.py', 'r') as file_object:
        line = file_object.readline()
    # you don't need to do the clean up explicity , and you don't need to call the finally 

def file_ensures_cleanup():
    file_object = open('FileOperations.py', 'r')
    if (file_object):
        try:
            line = file_object.readline()
        except:
            pass
        finally:
            file_object.close()

def file_write():
    file_object = open("myfile", 'w')
    file_object.write("Hello, world\n")
    file_object.close()    

def file_read_text_mode():
    file_object = open('myfile', 'r')
    count = 0
    while file_object.readline() != '':
        count = count + 1
    print(count)
    file_object.close()

def file_readlines_text_mode():
    file_object = open("FileOperations.py", 'r')
    count = len(file_object.readlines())
    file_object.close()

def file_read_bin_mode():
    input_file = open("myfile", 'rb') # the key point here is the 'rb' mode 
    header = input_file.read(4)
    data = input_file.read()
    input_file.close()
import sys

def print_file():
    # print can be redirect to any file , 
    f = open("outfile.txt", 'w')
    print("A first line.\n", "A second line\n", file = f)
    f.close()

def read_structure_binary_file():
    # the key point in th eparsing is 
    #  struct.calcsize
    #  struct.unpack 
    import struct
    record_format = 'hd4s'
    record_size = struct.calcsize(record_format)
    result_list = []
    input = open("data", 'rb')
    while 1:
        record = input.read(record_format)
        if record == '':
            input.close()
            break
        result_list.apend(struct.unpack(record_format, record))

def read_write_stdio():
    sys.stdout.write("Write to the standard output.\n")
    # this has the same effect as 
    print("Write to the standard output.\n")
    s = sys.stdin.readline()
    print("You have in put the ", s)
        
if __name__ == '__main__':
    file_open()
    file_deterministic_cleanup()
    file_ensures_cleanup()
    file_write()
    file_read_text_mode()
    file_readlines_text_mode()
