#!/usr/bin/python
#Gog annotation of common proteins and maybe and more 

import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)




file1= open("/Users/NikolasStrepis/Desktop/SzCommonForNikolas.csv")
file2=open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Proteomic_analysis/common_proteins/COG_annotation_common.txt")
file3=open("/Users/NikolasStrepis/Desktop/SzCommonforAndreia1.csv", "w")


dict1={}

dict2={}
list2=[]

#header= file1.readlines()
#file3.write(header+"\n")


for index,lines in enumerate(file1):
	#print lines
	identi = lines.strip().split("\t")[1]
	#print identi
	rest = lines.strip()
	dict1[identi]=rest

for index, lines in enumerate(file2):

	#print lines
	identi = lines.strip().split("\t")[0]
	list2=[identi]+list2

	info= lines.strip().split("\t")[1]
#	print info
	dict2[identi] = info


for key in dict1:

	for keys in dict2:
		#print [key], [keys]
		if key == keys:

			print dict2[keys] +"\t" +  dict1[key]+ "\n"
			file3.write(dict2[keys] +"\t" +  dict1[key]+ "\n")

#awesome trick for appending lines that do not met criteria


		if key not in list2:
			list2=[key]+list2


	#		print dict1[key] + "\n"
			file3.write( "\t" + dict1[key] + "\n")


