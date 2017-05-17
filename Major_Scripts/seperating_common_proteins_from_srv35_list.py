#!/usr/bin/python
#Script for isolating the 1vs2, 2vs3 etc and not including the 1vs1 from the srv 35% file. 

import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/data")
file2=open("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/multiple_hits_srv35.txt", "w")
file3=open("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/1vs1_hits_srv35.txt", "w")

dict1={}

dict2={}

list1=[]

list2=[]
infofull=[]

list3=[]

previous_lines=""
for index, lines in enumerate(file1):


	querya= lines.strip().split("\t")[0]

	queryb = previous_lines.split("\t")[0]

	
	previous_lines= lines.strip()
	info = lines.strip()

	if querya != queryb and "gi" in querya:
		dict1[querya]=info
		list1=[querya] + list1
	#	print "done"
	else:

		dict2[info]=querya


		list2 = [querya] + list2
for key in dict1:
	print key
	file3.write(dict1[key] + "\n")


print len(list1)
print len(list2)



file3.close