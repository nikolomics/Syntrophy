#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1= open("/home/nstrepis/Genomic_comparison/mergedblastp/SRV_35list")
file2 = open("/home/nstrepis/Genomic_comparison/Proteins/S.zhenderi_translated_proteins.fasta")
file3 = open ("/home/nstrepis/Genomic_comparison/common_zehnderi_sequences_zehn_wolfei.fasta", "w")



dict1={}
dict2={}

for index, lines in enumerate(file1):

	ref = lines.strip().split("\t")[1]
	cont= lines.strip().split("\t")[0]

	dict1[ref]=cont


for index, lines in enumerate(file2):


	if ">" in lines :

		seq= lines.strip()#.split(" ")[0].replace(">","")
		se1 = ""


	else:
		se1 = se1+ lines.strip()

	dict2[seq]=se1


for keys in dict1:
	for key in dict2:

		if keys in key:

			file3.write(key+" " + dict1[keys]+"\n"+dict2[key]+ "\n")





