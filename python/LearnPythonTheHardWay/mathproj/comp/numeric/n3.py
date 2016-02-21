'''
file: n3.py
description: this is a transformed of the n2.py which shows  you can do differently with the modules.
'''
from ... import version
from .. import c1
from . n2 import h
# from .n2 import h # this is the same as the line above

def g():
    print("version is", version)
    print(h())

