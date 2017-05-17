#!/usr/bin/python
#CSmall Script to count doimains that u may need from SAAP file 
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

a="IPR001753 IPR014748 IPR018376 IPR029045 | IPR001753 IPR029045 | IPR001753 IPR029045 | IPR001753 IPR029045 | IPR001753 IPR029045 | IPR001753 IPR014748 IPR018376 IPR029045 | IPR001753 IPR014748 IPR018376 IPR029045 | IPR001753 IPR018376 IPR029045 | IPR001753 IPR018376 IPR029045 | IPR001753 IPR014748 IPR018376 IPR029045 | IPR001753 IPR029045 | IPR001753 IPR018376 IPR029045 | IPR001753 IPR029045 | IPR001753 IPR014748 IPR018376 IPR029045 | IPR001753 IPR014748 IPR018376 IPR029045 | IPR001753 IPR014748 IPR029045 "
b=a.split("|")
numb =""

for i in b:

	i=i.count("IPR")
	numb =numb + "|" + str(i)

print numb