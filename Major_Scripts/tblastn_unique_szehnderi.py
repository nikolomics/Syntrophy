#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1= open("/home/nstrepis/Genomic_comparison/merged_s.zehnderi_acido/s.zehnderi_tblastn_acido.txt")
file2= open("/home/nstrepis/Genomic_comparison/tblastn_unique_sequences_zehnderi_acido.fasta" ,"w")
file3= open("/home/nstrepis/Genomic_comparison/results/s.zehnderi_tblastn.txt3")

dict1={}
dict2={}
dict3={}
info=""
contig=""

for index, lines in enumerate(file1):

	if "Query=" in lines:


		contig = lines.strip().split("\t")[0]
		indexa = int(index) + 6
		info2= lines.strip().split("\t")[10]
		info3 =lines.strip().split("\t")[11]
	#print contig, info
		dict1[contig] = info2 + "\t" + info3 + "\t" + info
list1=[]

for index, lines in enumerate(file3):
	#print lines
	contig = lines.strip().split("\t")[0]



	info  = lines.strip().split("\t")[1]
	info2= lines.strip().split("\t")[10]
	info3 =lines.strip().split("\t")[11]

	if contig not in list1:
		list1 = list1 + [contig]
		dict2[contig]=info2 + "\t" + info3 + "\t" + info
		#print list1

for keys in dict1:
	for key in dict2:
		#print [keys], [key]
		if keys==key:



			#print keys + "\t" + dict1[keys] + "\t" +dict2[key]+  "\n"
			file2.write(keys + "\t" + dict1[keys] + "\t" +dict2[key]+  "\n")






