# this is a formatter


'''
File: Formatter.py
Description: formatting a text based on open and closing parenthesis
Author: Joe

'''

import sys
import StringIO

def format():
	indent = 0
	char = sys.stdin.read(1)
	# StringIO.StringIO does not not have __exit__
	# with StringIO.StringIO() as output:
	output = StringIO.StringIO()
	newline = False
	while not char == "":
		if char == "\n":
			newline = True
		elif char == "{":
			indent += 1
		elif char == "}":
			indent -= 1

		if newline and char != "\n":
			output.write("  " * indent)
			newline = False
		output.write(char)
		char = sys.stdin.read(1)
	return output.getvalue();

def echo():
	indent = 0
	char = sys.stdin.read(1)
	output = StringIO.StringIO()
	while not char == "":
		output.write(char)
		print "in echo:"
		char = sys.stdin.read(1)
	value = output.getvalue();
	output.close()
	return vaue;


def write_stringio():
	output = StringIO.StringIO()
	output.write("hello world")
	value = output.getvalue()
	output.close()
	return value

if __name__ == "__main__":
	print (format())