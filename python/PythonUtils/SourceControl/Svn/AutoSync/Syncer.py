#!/usr/local/bin/python2.7
# encoding: utf-8
'''
SourceControl.Svn.AutoSync.Syncer -- Automatical Svn checking out tool

SourceControl.Svn.AutoSync.Syncer is a description

It defines classes_and_methods

@author:     user_name
        
@copyright:  2013 organization_name. All rights reserved.
        
@license:    license

@contact:    user_email
@deffield    updated: Updated
'''

import sys
import os
import subprocess


from os import path

from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter
from subprocess import Popen, check_call


__all__ = []
__version__ = 0.1
__date__ = '2013-10-16'
__updated__ = '2013-10-16'

DEBUG = 0
TESTRUN = 0
PROFILE = 1

SUCCESS = 0
ERR_SUCCESS = 0
ERR_MAKE_DIRS = 2
ERR_SVN_CO = 3



class ProgramNamepsace:
    pass


class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg

def main(argv=None): # IGNORE:C0111
    '''Command line options.'''
    def ensure_path(ns, p):
        if p is None or p == "":
            raise ValueError()
        try:
            if not path.exists(p):
                if hasattr(ns, "debug"):
                    print "makedirs {}".format(p)
                os.makedirs(p)
        except (IOError, os.error): # os.error is 
            ns.errmsg = "Failed to create directory at {}".format(p)
            return False
        return True
    
#     def svn_co(ns, url, root):
#         ns.cwd = None
#         try:
#             save_cwd(ns)
#             if not verify_has_trunk(url):
#                 raise ValueError("url should have trunk")
#             command = "svn co {}".format(url)
#             ensure_path(ns, root)
#             
#             
#             os.chdir(root)
#             os.system(command)
#         finally:
#             restore_cwd(ns)
    
    def svn_co(ns, url, root):
        if not url:
            raise ValueError("url")
        if not root:
            raise ValueError("root")
        try:
            cmd = "svn co {} {}".format(url, root)
            os.system(cmd)
        except Exception, e:
            sys.stderr.write("failed, reason: {}".format(e))

        
    def restore_cwd(ns):
        if ns is None: 
            raise ValueError("ns")
        if ns.cwd is not None:
            os.chdir(ns.cwd)
    def save_cwd(ns):
        if ns is None:
            raise ValueError("ns")
        ns.cwd = os.getcwdu()
    
    def verify_has_trunk(url):
        if url == None: # better use usl is None:
            raise ValueError("url")
        return url.endswith("trunk")
    
    # we can merge the svn_lists with the svn_exists into one function
    # by returning a tuple
    def svn_list(ns, url):
        cmd = "svn ls {}".format(url)
        pipe = Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout
        #  you cannot do the "assign and set" trick that you commonly do in other language , typically the C
        #because assignment in python is a "Statement" not a expression.
        #  check  How to assign a variable in IF, and then return it. (Python): http://stackoverflow.com/a/1551223
        # for the iteration recipe,check "reading text files:  http://effbot.org/zone/readline-performance.htm"
        while 1:
            line = pipe.readline()
            if line:
                yield line

    
    def svn_url_concat(url, sub_path):
        if not url: 
            raise ValueError("url")
        if not sub_path: 
            raise ValueError("sub_path")
        return url + sub_path
    
    def svn_exists(ns, url):
        if not url:
            raise ValueError("url")
        cmd = "svn info {}".format(url)
        return check_call(cmd) == 0

    
    def svn_pull(ns, url, root):
        '''
        Only plumb down one level
        '''
        if not verify_has_trunk(url):
            sub_urls = svn_list(ns, url)
            for sub_url_path in sub_urls:
                sub_url_path = sub_url_path.strip()
                sub_url = svn_url_concat(url, sub_url_path)
                sub_url_trunk = sub_url + "trunk"
                sub_root_to_trunk = path.join(root, sub_url_path, "trunk")
                if hasattr(ns, "debug") and ns.debug:
                    print "verify url: {}, root: {}".format(sub_url_trunk, sub_root_to_trunk)
                if verify_has_trunk(sub_url_trunk) and svn_exists(ns, url):
                    if hasattr(ns, "debug"):
                        print "svn co {} {}".format(sub_url_trunk, sub_root_to_trunk)
                    if hasattr(ns, "test") and ns.test:
                        continue
                    ensure_path(ns, sub_root_to_trunk)
                    svn_co(ns, sub_url_trunk, sub_root_to_trunk)
    
    
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2013 organization_name. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        parser.add_argument("root", action="store", help="the local root")
        parser.add_argument("url", action="store", help="the snv co url")
                      
        
        # Process arguments
        args = parser.parse_args()
        url = args.url
        root = args.root
        ns = ProgramNamepsace()
        ns.errmsg = ''
        
        # ensure the ae
        if not ensure_path(ns, root):
            print(ns.errmsg, sys.stderr)
            sys.exit(SUCCESS)
        
        # REMOVE: C:\dev\TEMP "http://path/to/your/repository/trunk"
        if root is None or root == '':
            raise ValueError("root is None or empty")
        
        ns.test = False
        ns.debug = True
        
        if url.endswith("trunk") or url.endswith("trunk/"):
            svn_co(ns, url, root)
        else:
            svn_pull(ns, url, root)
        
        
        return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
  


if __name__ == "__main__":
    if DEBUG:
        sys.argv.append("-h")
        sys.argv.append("-v")
        sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'SourceControl.Svn.AutoSync.Syncer_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())