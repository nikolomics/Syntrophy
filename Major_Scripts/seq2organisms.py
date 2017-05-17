#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for retrieving the sequences of S.zehnderi with coverage above 57 (graph defined) and of M.formicicum. 
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open("/home/nstrepis/Syntrophomonas_zehnderi/S.zehderi_Merged1_noscaffold_e/454ContigGraph.txt")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/S.zehderi_Merged1_noscaffold_e/454LargeContigs.fna", "r")
file3 = open ("/home/nstrepis/Syntrophomonas_zehnderi/S.zehderi_Merged1_noscaffold_e/454S.zehderi_seq.fasta", "w")
file4 = open ("/home/nstrepis/Syntrophomonas_zehnderi/S.zehderi_Merged1_noscaffold_e/454M.formiicum_seq.fasta" , "w")
dict1={}
dict2={}

for index,line in enumerate(file1):
	if index < 4208:
	#	print line.strip().split("\t")
		contig = line.strip().split("\t")[1]

		depth =line.strip().split("\t")[3]
	#	print depth

		if float(depth )> 57:
			dict1[contig] = depth
	#		print dict1[contig]
		else:
			dict2[contig] = depth
	#		print dict2[contig]
dict3={}
sequence=""
for index, line in enumerate(file2):

	if ">" == line[0]:
		if sequence:
			dict3[key]=sequence
	#	print lines.strip().split(" ")
		key=line.strip().split(" ")[0]
		sequence =""
	else:
		sequence += line.strip()
dict3[key] = sequence
print dict3

#	dict3[contig1]= seq
#	print dict3
for key in dict1:

	for keys in dict3:
	#	print [keys] ,[key]
		if key in keys:
			print "works"
			file3.write(keys + "\n" + dict3[keys] + "\n")
		#else:
			#print keys
for key in dict2:

	for keys in dict3:
		if key in keys:
			file4.write(keys + "\n" + dict3[keys] + "\n")