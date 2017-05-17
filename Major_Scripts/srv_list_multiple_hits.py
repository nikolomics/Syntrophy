#!/usr/bin/python
#Script for isolating the 1vs2, 2vs3 etc and not including the 1vs1 from the srv 35% file. 

import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/SRV_35list")
file2=open("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/multiple_hits_srv35.txt", "w")
file3=open("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/1vs1_hits_srv35.txt", "w")

dict1={}

dict2={}

list1=[]

list2=[]
infofull=[]

list3=[]
list4=[]

for index,lines in enumerate(file1):



	if "Query:" in lines:

		query= lines.strip()
		infofull=[]

	if "BLASTP" not in lines and "Fields" not in lines and "Query:" not in lines :


		info = lines.strip()

		infofull= [info] + infofull
	#	print infofull
		if len(infofull) !=1:
			dict1[query]=infofull
			#list4=[query]+list4
		#	print infofull ,"\n"
		else:
			#print infofull
			dict2[query] = infofull
			list3=[query]+list3



for key in dict1:
	list2=dict1[key]
	list1=[key] + list1
	if len(list2)!=0:
		#print list2
		#print list2
		#print "".join(list2)

		file2.write(key + "\t".join(dict1[key]) +"\n")

for key in dict2:
	if key in list3:


		file3.write(key + "\t"+ "\t".join(dict2[key]) + "\n")

print len(list1)
print len(list3)
file2.close