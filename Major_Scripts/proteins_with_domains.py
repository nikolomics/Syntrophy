#!/usr/bin/python
#CSmall Script to count doimains that u may need from SAAP file
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

a = sys.argv[1]


file1=open(a)


dict1={}
gene=""
tryt=""
for lines in file1:


	if "FT   gene            " in lines:


		gene = lines


		tryt=""
	else:
		tryt = lines + tryt
	
	dict1[gene] =tryt
ok=0
for key in dict1:

	#print dict1[key]
	if "Inter" in dict1[key]:


		ok =ok +  1


print ok
