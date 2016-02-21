'''
Created on Oct 17, 2013

@author: wangboqi

A dummy test program that shows how to deal string arguments.

'''



import argparse


parser = argparse.ArgumentParser() # don't forget the trailing ()
parser.add_argument("-v", "--verbosity", action="store_true", help="show verbose mode")
parser.add_argument("url", action="store", help="the snv co url")


args = parser.parse_args(args = None, namespace = None)

url = args.url;

if url:
    print "Url is {}".format(url)
