'''
Created on 2012-10-28

@author: Administrator
file: StringEssentials.py
description: StringEssentials.py shows essentials on the string
    Strings as sequence of characters
    Basic string operation
    Special characters and escape sequences
    Numeric (octal and hexadecimal) and Unicode escape sequences
    string methods 
      split and join
      converting strings to numbers
      strip 
      search
      modifying 
      Useful methods and constants
      converting from objects to string 
      Using the format method
    
'''

def string_as_list():
    x = 'Goodby\n'
    x = x[:-1]
    print("*** string as list, chop")
    print(x)
    y = len("Goodby\n")
    print("*** len(string)")
    print(y)

def basic_string():
    x = "Hello " + "World"
    print("*** basic_string")
    print(x)

def numeric_oct_hexadecimal_unicode_escape_sequence():
    print("*** normal string notation")
    x = 'm'
    print(x)
    print("*** octal notation")
    y = '\155'
    print(y)
    print("*** hexadecimal noation")
    y = '\x6D'
    print(y)
    # Because all string in Python3 are Unicode strings, they can also contain almost every character from 
    # every language avaiable. 
    # below show english name notation of Unicode
    print("*** named unicode notation") 
    unicode_a = '\N{LATIN SMALL LETTER A}'
    print(unicode_a)
    unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
    print(unicode_a_with_acute)
    print("*** unicode with number Unicode")
    unicode_a_with_acute_number= "\u00E1"
    print(unicode_a_with_acute_number)

def print_evaluate_string_with_special_character():
    print("*** print adds a newline to the end of the string")
    print("abc\n")
    print("*** end = \"\" cause the print NOT to append the newline")
    print("abc\n", end = "")

def string_method_split_join():
    print("*** str.join(...)")
    x = " ".join(["join", "puts", "spaces", "between", "elements"])
    print(x)
    x = "::".join(["Separated", "with", "colons"])
    print(x)
    x = "".join(["Separated", "by", "nothing"])
    print(x)
    # default, the split method will split on any whitespace
    x = 'You\t\t can have tabs\t\n \t and newlines \n\n ' \
        "mixed in"
    y = x.split()
    print("*** str.split()")
    print(y)
    y = "Mississippi"
    x.split("ss")
    x = 'a b c d'
    y = x.split(' ', 1)  # you can tell how many times split happens in the second argument

def string_convert_to_numbers():
    y = float('123.456')
    try:
        x = float('xxyy')
    except ValueError:
        pass
    y = int('3333')
    try:
        int('123.333')
    except ValueError:
        pass
    # you can change the radix of the expression 
    y = int('10000', 8)

def strip_string():
    print("*** strip()")
    x = "  Hello,    World\t\t "
    y = x.strip()
    print(y)
    print("*** lstrip()")
    y = x.lstrip()
    print(y)
    print("*** rstrip()")
    y = x.rstrip()
    print(y)

def string_module_constants():
    import string
    print("*** string constants")
    print(string.whitespace)

def string_searching():
    x = "Mississippi"
    y = x.find("ss")
    print("*** str.find()")
    print(y)
    y= x.rfind("ss")
    print("*** str.rfind()")
    print(y)
    x = "Mississippi"
    y = x.count("ss")
    print("*** str.count()")
    print(y)
    y = x.startswith("Miss")
    print("*** str.startswith")
    print(y)
    y = x.endswith("pi")
    print("*** str.endswith()")
    print(y)
    y = x.endswith(("i", "u"))

def string_replace():
    x = "Mississipi"
    x.replace("ss", "+++")
    print("*** str.replace") 
    x ="~x & (y % z)"
    table= x.maketrans("!*()", "!&[]")
    x.translate(table)
    print("*** maketrans")
    print(x)   
def methods_and_constants():
    x = "123"
    print("*** isdigit") 
    print(x.isdigit())
    print("*** isalpha")
    print(x.isalpha())
    x = "M"
    print("*** islower")
    print(x) 
    print("*** issupper")  
    print(x)

def convert_from_object_to_string():
    x = repr([1,2,3]) 
    print("*** repr")
    print(x)
    x = str([1, 2, 3])
    print("*** str")
    print(x)
def string_format():
    x = "{{Ambrosia}} is the {0} of {1}".format("food", "The gods")
    print("*** str.format")
    print(x)
    x = "{{Ambrosia}} is the {food} of {user}".format(food = "Ambrosia", user="the gods")
    print("*** str.format with name arguments")
    print(x)
    x = "{0} is the food of {user[1]}".format("Ambrosia", user = ["men", "the gods", "others"])
    print("*** str.format with name arguments")
    print(x)
    # advanced use of Format specified
    x = "{0:{1}} is the food of gods".format("Ambrosia", 10)
    print(x)
    x= "{0:{width}} is the food of gods".format("Ambrosia", width = 10)
    print(x)
    # >width is left justification
    x = "{0:>10} is the food of gods".format("Ambrosia")
    print(x)
    # <width is the right justification
    x = "{0:&<10} is the food of gods".format("Ambrosia")
    print(x)
    # besides the C# style of format, it also supports the C style format
    x = "%s is the %s of %s" % ("Ambrosia", "food", "The gods")
    print(x)
    num_dict = {'e': 2.718, 'pi': 3.14159}
    print("%(pi).2f - %(pi).4f - %(e).2f" % num_dict) # not that the name is in parenthesis

def control_print():
    #print, override the end separator
    print("a", "b", "c", end="\n\n")  
    #print , override the default sep 
    print("a", "b", "c", sep = "|")

      
if __name__ == '__main__':
    string_as_list()
    basic_string()
    numeric_oct_hexadecimal_unicode_escape_sequence()
    print_evaluate_string_with_special_character()
    string_method_split_join()
    string_convert_to_numbers()
    strip_string()
    string_module_constants()
    string_searching()
    string_replace()
    methods_and_constants()
    convert_from_object_to_string()
    string_format()
    control_print()