'''
Created on 2012-11-6

@author: Administrator
file: mymath, imp
descriptoin: to summarize, what is a module
  1. A module is a file defining Pyton objects
  2. If the name of the module file is modulename.py, then the Python name of the module is modulename.
  3. You can bring a module named modulename into use with the import modulename statement. After this statement is executed, objects defined in the module can be accessed as modulename.objectname.
  4. Specific names from a module can be brought directly into your program using the from modulename import objectname statement. This makes objectname accessible to your program without needing to 
     prepend it with modulename, and it's useful for bringing in names that are often used.
things to pay attention to:
    PYTHONPATH
    sys.path
    sys.prefix
    
you can put one. pth file under the path pointed by the sys.prefix, it contains path where the python can search and load python module from     
'''

def module_search_path():  
    # it is configurable that sys.path is initialized from the following values. 
    #  1. PYTHONPATH
    #  2. the directory containing the current executing script will be searched first. if sys.path is set to empty string, it should take as meaning that it shall first look for modules in the current directory
    # 
    import sys
    x = sys.path
    print("*** module search path")
    print(x)
    x = sys.prefix
    print("*** module prefix path")
    print(x)


def module_namespace():
    

if __name__ == '__main__':
    import Modules.mymath, imp
    # import again will not reload a modified module
    # you may need imp.reload method to reload the module
    imp.reload(Modules.mymath)
    module_search_path()