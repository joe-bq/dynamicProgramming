'''
Created on 2012-11-20

@author: Administrator
'''

import re

def replace_basic():
    string = "If the the problem is textual, use the the re module"
    pattern = r"the the"
    regexp = re.compile(pattern)
    substituted = regexp.sub("the", string)
    print("*** after replacement, the string is {0}".format(substituted))

def replace_advanced_func():
    int_string = "1 2 3 4 5"
    
    def int_match_to_float(match_obj):
        return (match_obj.group('num') + ".0")    
    pattern = r"(?P<num>[0-9]+)"
    regexp = re.compile(pattern)
    substituted = regexp.sub(int_match_to_float, int_string)
    print("**** after replacement, the string is {0}".format(substituted))

if __name__ == '__main__':
    replace_basic()
    replace_advanced_func()
