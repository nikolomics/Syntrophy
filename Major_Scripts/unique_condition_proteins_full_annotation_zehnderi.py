#!/usr/bin/python
#Nikolas Strepis 4-2014
#Best script for blast matches it can use the general form and take the best hit!!
import os, sys ,fnmatch , numpy

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1= open("/Users/NikolasStrepis/Dropbox/Publication/extra_data/stearate_annotation2.csv")

file2= open("/Users/NikolasStrepis/Dropbox/Publication/extra_data/oleate_annotation2.csv")


file3= open("/Users/NikolasStrepis/Desktop/unique_stereate.csv", "w")

file4= open("/Users/NikolasStrepis/Desktop/unique_oleate.csv", "w")



dict1={}
dict2={}

list1=[]
list2=[]
for index, lines in enumerate(file1):


	contig=lines.strip().split(";")[0]
	#print [contig]
	info=lines.strip()

	list1=[contig] + list1
	dict1[contig]=info


for index, lines in enumerate(file2):




	contig=lines.strip().split(";")[0]

#	print [contig]

	info=lines.strip()

	list2=[contig] + list2
	dict2[contig]=info


for key in dict1:

	if key not in list2:

		print key
		file3.write(dict1[key] + "\n")



for key in dict2:


	if key not in list1:


		file4.write(dict2[key]+ "\n")

