#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1= sys.argv[1]
file2= sys.argv[2]

input1= open(file1)
output2=open(file2, "w")
dict1={}
indexa=""
for index, lines in enumerate(input1):


	if "Query= " in lines:

		protein = lines.strip().split(" ")[1]

	if ">" in lines :
		indexa = index + 1
		match =""

		match = lines.strip().split("> ")[1]
	if index == indexa	:

		match = match + " " + lines.strip()

		dict1[protein] = match

for key in dict1:
	output2.write(key + "\t"  + dict1[key] +"\n")



output2.close




