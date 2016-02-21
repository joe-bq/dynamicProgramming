'''
Created on 2012-11-7

@author: Administrator
file: optparse.py
description:this file optparse.py demonstrate the use of the OptionParse module, which is a module that helps you to parse and process of the Option, we used to have the optine
   parse_arg
   return value of the parse_arg

'''

from optparse import OptionParser
def main():
    parser = OptionParser()
    parser.add_option("-f", "--file", dest = "filename", 
                      help = "write report to FILE", metavar = "FILE")
    parser.add_option("-x", "--xray", dest = "xray", 
                      help = "specify xray strength factor")
    parser.add_option("-q", "--quiet", action="store_false", dest = "verbose", default = True, 
                      help = "don't print status message to stdout")
    
    (options, args) = parser.parse_args()
    
    print("options:", str(options))
    print("arguments:", args)

if __name__ == '__main__':
    print("optparse method ")
    main()