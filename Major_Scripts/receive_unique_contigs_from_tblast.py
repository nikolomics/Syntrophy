#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open ("/home/nstrepis/Genomic_comparison/merged_s.zehnderi_acido/S.zehnderi_unique.txt")
file3= open("/home/nstrepis/Genomic_comparison/Proteins/S.zhenderi_translated_proteins.fasta")
file2 = open ("/home/nstrepis/Genomic_comparison/unique_szehnderi_sequences_zhenderi_acido.fasta" , "w")

dict1={}

for index, lines in enumerate(file1):

	contig = lines.strip().split("\t")[0]

	dict1[contig]=contig

dict2={}

for index, lines in enumerate(file3):

	if ">" in lines :

		contig = lines.strip()
		seq=""
	#	print contig
	else:
		seq=seq +lines.strip()
		dict2 [contig] = seq

for keys in dict1:

	for key in dict2:
		#print [key], [keys]
		if keys in key:

			file2.write(key + "\n" + dict2[key] + "\n")




