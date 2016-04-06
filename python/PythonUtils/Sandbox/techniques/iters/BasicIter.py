'''
Created on Oct 17, 2013

@author: author

NOTE: show how to build iterators. 

TODO: consider howt o implements some infinite elements.
'''


class Counter:
    '''
    Counter as a iterator class
    '''
    def __init__(self, low, high):
        self.current = low
        self.high = high
    def __iter__(self):
        return self
    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1
for c in Counter(3, 8):
    print c
# generaotr function
def counter(low, high):
    '''
    counter as a generator function
    '''
    current = low
    while current <= high:
        yield current
        current += 1

for c in Counter(3, 8):
    print c
    

# generator
def uc_get(text):
    '''
    uc_get: get uppercase in generator
    '''
    for char in text:
        yield char.upper()
    
#generator expression
def uc_getexp(text):
    '''
    uc_getexp: get upper case in generator expression
    '''
    return (char.upper() for char in text)

for c in uc_getexp("he"):
    print c

#iteraor protocol
class uc_iter():
    '''
    uc_iter: class implement the iter protocol
    '''
    def __init__(self, text):
        self.text = text;
        self.index = 0
    def __iter__(self):
        return self
    def next(self):
        return self.__next__()
        #return __next__()
    def __next__(self):
        try:
            result = self.text[self.index].upper()
        except IndexError:
            raise StopIteration
        self.index += 1
        return result

for c in uc_iter("he"):
    print c
#getitem method
class uc_getitem():
    def __init__(self, text):
        self.text = text
    def __getitem__(self, index):
        result = self.text[index].upper()
        return result
    