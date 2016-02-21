'''
Created on 2012-10-31

@author: Administrator
file: ByteEssentials.py
description: ByteEssentials.py  demonstrate hte use of 
   encode
   decode
'''

def byte_basics():
    unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
    print(unicode_a_with_acute)
    xb = unicode_a_with_acute.encode()
    print(xb)
    try:
        xb += 'A'
    except:
        print("can't concat bytes to str")
        pass
    converted_back = xb.decode()
    print(converted_back)


if __name__ == '__main__':
    byte_basics()