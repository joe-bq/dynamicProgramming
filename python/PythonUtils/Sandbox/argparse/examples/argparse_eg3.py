'''
Created on Oct 17, 2013

@author: wangboqi

a clone of the example of argparse_eg2.py, with one change to the type of verbosity option argument. 
the type of the verbosity is changed from int to true..

References: 
    http://docs.python.org/2/howto/argparse.html

'''



import argparse


parser = argparse.ArgumentParser() # don't forget the trailing ()
#parser.add_argument("square", type=int, help="display a square of agiven nubmer")
parser.add_argument("x", type=int, help="power base")
parser.add_argument("y", type=int, help="power exponent")
#parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="display a square of agiven nubmer")
# you can not add the type kwargs with action is "store_true"..
parser.add_argument("-v", "--verbosity", action="store_true", help="show verbose mode")


args = parser.parse_args(args = None, namespace = None)

#answer = args.square ** 2;
answer = args.x ** args.y

if args.verbosity:
    print "power {} of {} is {} ".format(args.x, args.y, answer)
else:
    print "{} ^ {} is {}" .format(args.x, args.y, answer)
