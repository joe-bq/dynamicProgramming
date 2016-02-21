'''
Created on 2012-11-17

@author: Administrator
file: DiskWritingExample.py
description: this file will demonstrate the use of the Exception used in the common programming patterns
'''
def save_to_file(filename):
    try:
        save_text_to_file(filename)
        # save_formats_to_file(filename)
        # save_prefs_to_file(filename)
    except IOError:
        # handle the error ....
        pass


def save_text_to_file(filename):
    pass


if __name__ == '__main__':
    pass