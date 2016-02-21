'''
Created on 2012-11-4

@author: Administrator
file: FunctionEssentials.py
description: this file is to demonstrate the use of the function inside Python
   function basics
   variable number of arguments
   argument by keyword
   and use of mixed keyword
   different way of calling variable argument and keyword arguments (direct and use of * and ** operator)
'''


def fact(n):
    """Return the factorial of the given number."""
    r = 1
    while n> 0:
        r = r * n
        n = n - 1
    return r;

def function_position_parameters():
    def power(x, y):
        r = 1
        while y > 0:
            r = r * x
            y = y - 1
        return r
    print("*** position parameter (x, y)")
    print(power(3, 3))
    
    def power_default_values(x, y = 2):
        r = 1
        while y > 0:
            r = r * x
            y = y - 1
        return r;
    print("*** position parameter (x, y = 2")
    print(power_default_values(3))
    
    def passing_parameter_by_name():
        print("*** passing by parameter name (x = 2, y = 3")
        print(power_default_values(x = 2, y = 3))
    passing_parameter_by_name()

def variable_number_arguments():
    def maximum(*numbers):
        if len(numbers) == 0:
            return None
        else:
            maxnum = numbers[0]
            for n in numbers[1:]:
                if n > maxnum :
                    maxnum = n
            return maxnum    
    print("*** variable length paramer : (*numbers)")
    print(maximum(*(1, 2, 3, 4, 6)))
    print("*** this is another way to call it: ([numbers])")
    print(maximum(1, 2, 3, 4, 5))

def argument_by_keyword():
    def example_fun(x, y , **other):
        print("x:{0}, y:{1}, keys in 'other': {2}".format(x, y, list(other.keys())))
        other_total = 0
        for k in other.keys():
            other_total = other_total + other[k]
        print("The total of values in 'other' is {0}".format(other_total))
        return other_total
    print("*** keyed arguments")
    print(example_fun(1, 2, a = 2, b = 3, c = 4))
    print("** another way of using keyed arguments")
    print(example_fun(1, 2, **{"a": 2, "b" : 3, "c" : 4}))

def mixed_argument_passign_techniques():
    pass

if __name__ == '__main__':
    print("*** function definition ")
    x = fact(5)
    print(x)
    function_position_parameters()
    variable_number_arguments()
    argument_by_keyword()