#!/usr/bin/python
#Script for retrieving the first hit from the blast annotation, takes more thna the ...

import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/Gene_Comparison/blastp_results/blastp_szehnderi_unique_sequences.txt")

file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/Gene_Comparison/S.zehnderi_unique_best_blastp_hits.txt", "w")


dict1=dict()
dict2={}

list1=[]
list2=[]

full_protein =""
full_annot=""
for index, lines in enumerate(file1):


	protein = lines.strip().split("\t")[0]
	annot = lines.strip().split("\t")[1]
	list2 = list2 +[protein]
	evalue = lines.strip().split("\t")[11]
	score=lines.strip().split("\t")[10]

	full = annot + "\t" + evalue  + "\t" + score

	if protein in dict1:

	
		dict1[protein].append(full)

	else:

		dict1[protein] = [full]
	

	# list1= list1 + [evalue]
	# if list2[0] != protein:
	# 	list2=[]
	# 	list1=[]
	# 	full_protein =""
	# 	full_annot =""
	


	#  #print len(list1)

	# #print list1
	# #print list1
	# for i in list1:



	# 	if  float(i) == float(list1[0]) :
	# 	#	print float(i), float(list1[0])

	# 		full_protein = protein 

	# 		full_annot =full_annot +"\t" +  annot 




	# 		dict1[full_protein] = full_annot
list3=[]  
key = ""
for key in dict1:
	list3=dict1[key]

	selected_annot = "\t".join(list3[0:3])
	#print selected_annot


	file2.write(key + "\t" + selected_annot + "\n")
	print key + "\t" + selected_annot + "\n"
#	print key + "\t" + dict1[key] + "\n"

file2.close

