'''
Created on 2012-10-25

@author: Administrator
file: ListEssentials.py
description: ListEssentials.py demonstrate the 
   indice
   modifying lists
   sorting lists
   custom sorting
   sorted() function
   list membership
   +, *
   search
   matchs
   shallow copies and deep copies
'''

def list_indices():
    x = ["first", "second", "third", "fourth"]
    print("*** first element")
    print(x[0]);
    a = x[-1];
    print("*** last element")
    print(a);
    print("*** first element to last element")
    print(a[1 : -1])
    
def modify_lists():    
    x = [1,2 ,3, 4]
    x[1] = "two"
    print("*** after modifying first element")
    print(x)
    x[len(x):] = [5, 6, 7]
    print("*** after append a list")
    print(x)
    x[:0] = [-1, 0]
    print("*** after prepend a list")
    print(x)
    x[1:-1] = []
    print("*** after remove elements from list")
    print(x)
    x = [1, 2, 3]
    x.append("four")
    print("*** append one element with append")
    print(x)
    y = [5, 6, 7]
    x.extend(y)
    print("*** append one list with extend")
    print(x)
    x.insert(2, "hello")
    print("*** after insert element to the second index")
    print(x)
    x[2:2] = ["hello"]  # don't write as x[2;2] = "hello" it will treat each element of 'hello' as eleemnts of x
    print("*** insert is the same as x[n:n]")
    print(x);
    print("*** insert with negative index")
    x.insert(-1, "hello")
    print(x)
def del_lists():
    x = [1, 2, 3, 4]
    del x[1]
    print("*** after delete the second elements")
    print(x)
    print("*** delete list from list")
    del x[:2]
    print(x)
    print("*** delete the variable ")
    del x    
    if ('x' not in vars()):
        print('x is deleted')
    x = [1, 2, 3, 4, 5, 6]
    x.remove(3)
    print("**** after the list.remove() called")
    print(x)

def reverse_list():
    x = [1, 2, 3, 4]
    print("*** before the reverse")
    x.reverse()
    print("*** after reverse")
    print(x)

def sort_list():
    x = [3, 8, 4, 0, 2, 1]
    x.sort()
    print("*** x.sort()")
    print(x)
    x= [2, 4, 1, 3]
    y = x[:]   # make a copy 
    y.sort()
    print("*** after sort on the copy")
    print(y)

def compare_num_of_chars(string1):
    return len(string1)
    
def custom_sort():
    word_list = ['Python', 'is', 'better',  'than', 'c']
    word_list.sort()
    print(word_list)
    word_list = ['Python', 'is', 'better',  'than', 'c']
    word_list.sort(key = compare_num_of_chars)
    print(word_list)
    word_list = ['Python', 'is', 'better',  'than', 'c']
    word_list.sort(key = compare_num_of_chars, reverse = True)
    print(word_list)
    x = [4, 3, 1, 2]
    y = sorted(x)
    print(y)


def membership_in_list():
    x = 3 in [1, 3, 4, 5]
    print ("*** 3 in [1, 3, 4, 5] =  ", x)
    x = 3 not in [1 ,3 , 4, 5]
    print ("*** 3 no tin [1, 3, 4, 5] = ", x)

def concat_list():
    z = [1, 2, 3] + [4, 5]
    print("*** concat")
    print(z)

def list_init():
    z = [None] * 4
    print("list init")
    print("*** [None] * 4 = ", z)
    z = [3, 1] * 2
    print("*** [3, 1] * 2 = ")
    print (z)

def min_and_max():
    x = min([3, 7, 0, -2, 11])
    print("*** min")
    print(x)
    print("*** max")
    # you can do max on the isomorphic list elements
    #y= max([4, "hello", [1, 2]])

def search_and_index():
    x = [1, 3, "five", 7, -2]
    print("*** index")
    y = x.index(7)
    print(y)
    try:
        y = x.index(5)
        print(y)
    except ValueError:
        print("Exception ValueError")
        pass
def match_and_count():
    x = [1, 2, 2, 3, 5, 2, 5]
    y = x.count(2)
    print("*** count")
    print(y)
    y = x.count(5)
    y = x.count(4)

def nested_lists_and_deep_copy():
    m = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    print(m[0])
    print(m[0])
    print("*** m[0][1]")
    print(m[0][1])    
    print("*** original")
    nested = [0]
    original = [nested, 1] 
    print(original)
    print("*** shallow copy")
    shallow = original[:]
    import copy 
    deep = copy.deepcopy(original)
    print("*** deep copy")
    print(deep)
    deep[0][0] = 'zero'
    print("*** modify the deep copy ")
    print(original)
    shallow[0][0] ='zero'
    print("*** modify shallow copy")
    print(original)
    
if __name__ == '__main__':
    list_indices()
    modify_lists()
    del_lists()
    reverse_list()
    sort_list()
    custom_sort()
    concat_list()
    list_init()
    min_and_max()
    search_and_index()
    match_and_count()
    nested_lists_and_deep_copy()