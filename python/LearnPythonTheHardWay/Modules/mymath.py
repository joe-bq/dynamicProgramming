'''
Created on 2012-11-6

@author: Administrator
file: mymath.py 
description: this file is a user module, where in ohter modules, we will demonstrate how to import and use this module
'''
"""mypath - our example math module"""
pi = 3.14159
def area(r):
    """area(r): return the area of a circle with radius r."""
    global pi
    return (pi * r * r)
