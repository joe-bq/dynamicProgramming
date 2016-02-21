'''
Created on 2012-11-16

@author: Administrator
file: ShelvesOperation.py
description: this file will demonstrate the use of the shelv object 
   what is shelve? shelves is something that gives you some basic  persistence so you will be able to retrieve what you have shelved in last session
   
'''

import shelve
def demon_shelve():
    book = shelve.open("addresses")
    book['flintstone'] = ('fred', '555-1234', '1233 Bedrock Place')
    book['rubble'] = ('barney', '555-4321', '1235 Bedrock Place')
    book.close()
    
    
def shelve_out():
    book = shelve.open("addresses")
    if 'flintstone' in book:
        flintstone = book['flintstone']
        print("*** after retrieved the shelves")
        print(flintstone)
        rubble = book['rubble']
    book.close()

if __name__ == '__main__':
    book = shelve.open("addresses")
    exists = 'flintstone' in book
    book.close()
    if exists:
        shelve_out()
    else:
        demon_shelve()
    