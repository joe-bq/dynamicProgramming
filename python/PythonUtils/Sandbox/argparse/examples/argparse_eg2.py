'''
Created on Oct 17, 2013

@author: wangboqi
'''



import argparse


parser = argparse.ArgumentParser() # don't forget the trailing ()
#parser.add_argument("square", type=int, help="display a square of agiven nubmer")
parser.add_argument("x", type=int, help="power base")
parser.add_argument("y", type=int, help="power exponent")
parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="display a square of agiven nubmer")


args = parser.parse_args(args = None, namespace = None)

#answer = args.square ** 2;
answer = args.x ** args.y

if args.verbosity > 1:
    print "power {} of {} is {} ".format(args.x, args.y, answer)
else:
    print "{} ^ {} is {}" .format(args.x, args.y, answer)
