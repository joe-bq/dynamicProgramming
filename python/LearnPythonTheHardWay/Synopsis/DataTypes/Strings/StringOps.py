'''
Created on 2012-10-22

@author: Administrator
file: StringOps.py
description: this file will demonstrate the use
'''
def string_and_ops():
    x = "live and    let \t   \t live"
    y = x.split()
    print ("*** x.split()")
    print(y)
    z = x.replace("let \t   \t live", "enjoy life")
    print("*** after the string replace")
    print(z)
    import re  # actually you can do the import anywhere
    regexpr = re.compile(r"[\t ]+")
    o = regexpr.sub(" ", x)
    print("*** after the re replacement")
    print(o)
def string_and_print():
    e = 2.718
    x = [1, "two", 3, 4.0, ["a", "b"], (5, 6)]
    print("The constant e is :", e, "and the list x is:", x) # print with the default format 
    print("the value of %s is: %.2f" % ("e", e)) # the c printf style of print

if __name__ == "__main__":
    string_and_ops()    
    string_and_print()