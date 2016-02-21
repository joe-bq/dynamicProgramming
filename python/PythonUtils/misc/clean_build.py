'''Clean folders by walking the directory and call msbuild /t:clean on each directory
'''


import os
import sys
from os.path import splitext, join, isfile, isdir, basename
from os import walk, system, listdir, unlink
from shutil import rmtree


def clean_build(path, configuration):
	print("calling msbuild /t:clean /p:Configuration={1} on '{0}'".format(path, configuration))
	system("msbuild /t:clean /p:Configuration={1} {0}".format(path, configuration))

def clean_build_devenv(path):
	system("devenv {0} /Clean".format(path))

# Python recursive folder read - which we don't quite need. 

rootdir = sys.argv[1]

#for foldr, subs, files in os.walk(rootdir):
#	'''simple logic to filter out .sln files'''
#
#	has_sln = False
#	for file in files:
#		# do concatenation to get full path
#		full_path = join(root, file)
#		ext = splitext(full_Path)
#		if ext == ".sln":
#			clean_build(full_path)
#			has_sln = True
#	if has_sln:

def visit(rootdir):
	if rootdir == None or not isdir(rootdir):
		return
	for item in os.listdir(rootdir):
		'''simple logic to filter out .sln files'''
		has_sln = False
		full_path = join(rootdir, item)
		if isfile(full_path):
			ext = splitext(full_path)[1]
			if ext == ".sln":
				print("Clean {0}".format(full_path))
				clean_build(full_path, "Release")
				clean_build(full_path, "Debug")
				clean_build_devenv(full_path)
				has_sln = True
		if isdir(full_path):
			print("visiting {0}".format(full_path))
			visit(join(full_path))
		if has_sln:
			return


def visit_generic(rootdir, predicate, action):
	if rootdir == None or not isdir(rootdir):
		return
	for item in os.listdir(rootdir):
		'''simple logic to filter out .sln files'''
		full_path = join(rootdir, item)
		if predicate(full_path):
			action(full_path)
		if isdir(full_path):
			visit_generic(full_path, predicate, action)

def is_dependencies_folder(rootdir):
	if rootdir == None or not isdir(rootdir):
		return False
	if isdir(rootdir):
		base = basename(rootdir)
		if base.lower() == "dependencies":
			return True;
	return False

def is_vc_deletable_file(file):
	if file == None or not isfile(file):
		return False
	if isfile(file):
		ext = splitext(rootdir)[1]
		if ext == ".sdf" or ext == ".ipch" :
			return true;
	return False

def remove_file(file):
	if file == None or not isfile(file):
		return
	if isfile(file):
		unlink(file)

def remove_dir(rootdir):
	if rootdir == None or not isdir(rootdir):
		return
	if isdir(rootdir):
		print "Removing {0}".format(rootdir)
		rmtree(rootdir)

#visit(rootdir)
visit_generic(rootdir, is_dependencies_folder, remove_dir)
visit_generic(rootdir, is_vc_deletable_file, remove_file)