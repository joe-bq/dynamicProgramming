'''
Created on 2012-11-5

@author: Administrator
file: ScopeEssentials.py
description: ScopeEssentials.py demonstrate the use of the Scope variables. 
   Local - the default scope , which will declared when it is first used, later reference will use the local one 
   Nolocal - binds to the previously bound variables in the closest closing scope
   Global variables- binds to the global variables
   
'''


g_var = 0      # g_var in inner_test binds top-level g_var
nl_var = 0
print("top level -> g_var: {0} nl_var : {1}".format(g_var, nl_var))
def test():
    nl_var = 2  # bind to the top-level g_var
    print("in test-> g_var: {0} nl_var: {1}".format(g_var, nl_var))
    print("in test->g_var:{0} nl_var: {1}".format(g_var, nl_var))
    def inner_test():
        global g_var             ### 'global' keyword will bind the g_var to the top-level g_var
        nonlocal  nl_var         ### nl_var in inner_test binds to nl_var in test 'nonlocal" binds to the previously bound variables in the closing scope. 
        g_var = 1
        nl_var = 4
        print("in inner_test -> g_var :{0} nl_var : {1}".format(g_var, nl_var))
    inner_test()
    print("in test->g_var: {0} nl_var : {1}".format(g_var, nl_var))

test()
print("top level -> g_var :{0} nl_var : {1}".format(g_var, nl_var))    

if __name__ == '__main__':
    pass