#!/usr/bin/python
#CSmall Script to count doimains that u may need from SAAP file 
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

a = sys.argv[1]


b=a.split("|")

for i in b:

	print i