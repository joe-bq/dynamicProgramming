'''
Created on 2012-11-5

@author: Administrator
file: LambdaEssentials.py
description: LambdaEssentials.py demonstrate the use of Lambda usage
    lambad is something you see in functional programming, some OO oriented languages has possed some trait of functional languages, such as C#
'''

def f_to_kelvin(degrees_f):
    return 273.15 + (degrees_f - 32) * 5 / 9
def c_to_kelvin(degrees_c):
    return 273.15 + degrees_c

if __name__ == '__main__':
    t2 = {'FtoK': lambda deg_f : 273.15 + (deg_f - 32) * 5 / 9, 
          'CtoK': lambda deg_c : 273.15 + deg_c}
    x = t2['FtoK'](32)
    print("*** lambda used as function call")
    print(x)