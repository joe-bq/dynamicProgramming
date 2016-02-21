'''
Created on 2012-10-23

@author: Administrator
file: FileExceptionExapmle.py
description: this file will demonstrate the use of exception system in Python
'''

class EmptyFileError(Exception):
    pass

def open_file():
    filenames = ['myfile1', 'nonExistent', "emptyFile", "myfile2"]
    for file in filenames:
        try:
            f = open (file, 'r')
            line = f.readline()
            if line == "":
                f.close()
                raise EmptyFileError("%s: is empty" % file)
        except IOError as error:
            print("%s: could not be opened : %s" % (file, error.strerror)) # strerror is a common property of Exception or is strerror IOError specific
        except EmptyFileError as Error:
            print(error)                                                   # a common thing to do is the print(Error), though you can use traceback to get more controls
        else:
            print("%s : %s" % (file, f.readline()))
        finally:
            print("Done processing", file)

if __name__ == '__main__':
    open_file()