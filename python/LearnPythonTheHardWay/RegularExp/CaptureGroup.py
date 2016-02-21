'''
Created on 2012-11-19

@author: Administrator
'''
import re

if __name__ == '__main__':
    regexp = re.compile(r"(?P<last>[-a-zA-Z]+),"
                    r" (?P<first>[-a-zA-Z]+)"   
                    r"( (?P<middle>([-a-zA-Z]+)))?" 
                    r": (?P<phone>(\d\d\d-)?\d\d\d-\d\d\d)"
                    )
    file = open("textfile2", 'r')
    for line in file.readlines():
        result = regexp.search(line)
        if result == None:
            print("Oops, I don't think this is a record")
        else:
            lastname = result.group('last')
            firstname = result.group('first')
            middlename = result.group('middle')
            if middlename == None:
                middlename = ""
            phonenumber = result.group('phone')
            print('Name: {0} {1} {2} number: {3}'.format(firstname, middlename, lastname, phonenumber))
    file.close()