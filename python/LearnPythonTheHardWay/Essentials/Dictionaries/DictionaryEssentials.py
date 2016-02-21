'''
Created on 2012-10-31

@author: Administrator
file: DictoinaryEssentials.py
description: DictionaryEssentials.py
  dictionary basics
  update method
  copy method
  dictionary membership 
  dictionary use case 1  - work count
  dictionary use case 2 - cache
  dictionary use case 3 - sparse matrix 
  dictionary key type requirement
'''

def dictionary_basic():
    english_to_french = {'red' : 'rougue', 'blue' : 'bleu', 'green' : 'vert'}
    print("*** len of dictionary")
    # the view object of the Dictionary view object
    # keys, values, items, which is updated each time the dictionary is changed. 
    print(len(english_to_french))
    print("*** dictionary keys")
    print(list(english_to_french.keys()))
    print("*** dictionary values")
    print(list(english_to_french.values()))
    print("***dictionary items")
    print(list(english_to_french.items()))
    
    # del an item from the 
    del english_to_french['green']
    
    # get or default 
    x = english_to_french.get('blue', "No translation")
    print(x)
    x = english_to_french.get('chartreuse', 'No translation')
    print(x)
    x = english_to_french.setdefault('chartreuse', 'No translation')
    print(x)

def udpate_dictionary():
    z = {1 : 'One', 2 : 'Two'}
    x = {0 : 'Zero', 1: 'one'}
    x.update(z)
    print(x)

def copy_dictionary():
    x = {0: 'zero', 1: 'one'}
    y = x.copy()
    print(y)

def dictionary_membership():
    english_to_french = {'red' : 'rougue', 'blue' : 'bleu', 'green' : 'vert'}
    x = 'red' in english_to_french
    print("*** membership 'in' in dictionary")
    print(x)   
        
def dictionary_use_case1():
    sample_string= 'To be or not to be'
    occurrences = {}
    for word in sample_string.split():
        occurrences[word] = occurrences.get(word, 0) + 1
    for word in occurrences:
        print("The word", word, 'occurs', occurrences[word], "tiemes in teh string")        

def what_can_be_dictionary_key():
    # python dictionary key must meet the following two conditions
    #   hashable
    #   immutable
    # in this condition, list cannot be the key, however, sometimes it is neccessary to 
    # have key of list type, in this case, python solve the problem by 
    # immutable list, tuple.
    # if you wna to have set as the key to dictionary, you can use the frozenset
    #
    pass

def dictionary_use_case2_sparse_matrix():
    rownum = 1
    colnum = 1
    matrix =  [[3, 0, -2, 11], [0, 9, 0, 0], [0, 7, 0, 0], [0, 0, 0, -5]]
    element = matrix[rownum][colnum]
    print("*** matrix")
    print(element)
    matrix = {(0, 0): 3, (0, 2): -2, (0, 3) :11, 
              (1, 1): 9, (2, 1): 7, (3, 3): -5 }
    if (rownum, colnum) in matrix:
        element =  matrix[(rownum, colnum)]
    else:
        element = 0;
    print("*** sparse matrix with dictionary")
    print(element)

def dictionary_use_case3_cache():
    sole_cache = {}
    def sole(m, n, t):
        if (m, n, t) in sole_cache:
            return sole_cache[(m, n, t)]
        else:
            # ... do some time consuming calculating
            result = 'a'
            sole_cache[(m, n, t)] = result
            return result;    
          
if __name__ == '__main__':
    dictionary_basic()
    udpate_dictionary()
    dictionary_membership()
    dictionary_use_case1()
    what_can_be_dictionary_key()
    dictionary_use_case2_sparse_matrix()
    dictionary_use_case3_cache()