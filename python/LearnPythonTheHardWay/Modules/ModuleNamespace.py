'''
Created on 2012-11-6

@author: Administrator
file: ModuleNamespace.py
description: Modules has three types of namespace
   locals() : local namespace 
   globals() : global namespace is looked in next
   __builtins__: built-in namespace 
'''


def namespace_case1():
    z = 2
    import math
    from cmath import cos
    x = globals()
    print("*** after import, globals")
    print(x)
    x = locals()
    print("*** after import, locals ")
    print(x)
    x = math.ceil(3.4)
    del z, math, cos  # you can actually remove modules.
    x = locals()
    print(x)

if __name__ == '__main__':
    namespace_case1()