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
file3 = sys.argv[3]


input1= open(file1)
input2=open(file2)
output=open(file3, "w")
dict1={}
dict2={}

for index, lines in enumerate(input1):


	contig = lines.strip().split("\t")[0]
#	print contig
	peptides = lines.strip().split("\t")[6]
	#print peptides

	dict1[contig] = peptides


for index, lines in enumerate(input2):


	contig = lines.strip().split("\t")[0]

	sente = lines.strip()


	dict2[contig] = sente


for key in dict1:

	for keys in dict2:


		if key == keys:


			print key + "\t" +dict2[keys] + "\t" + dict1[key]



			output.write(key + "\t" + dict2[keys] + "\t" + dict1[key] + "\n")
output.close