#!/usr/bin/python
#Script for retrieving sequences after seperating unique, common and 2vs1 in the zehnderi and wolfei comparison.

import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/Gene_Comparison/S.zehnderi_unique.txt")
file2=open("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/S.zehnderi_prodigal_sspace_proteins.fasta")
file3 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/Gene_Comparison/S.zehnderi_unique_sequences.fasta", "w")


dict1={}
dict2={}
list1=[]
list2=[]
for index,lines in enumerate(file1):


	query = lines.strip()

	dict1[query]=query


for index, lines in enumerate(file2):



	if ">" in lines :

		query = lines.strip().split("#")[0].replace(" ","").replace(">","")
		print query
		seq = ""

	else:


		sequence = lines.strip()
		#print sequence
		seq = str(sequence) + seq

		dict2[query]= sequence


for key in dict1:
	print key
	for keys in dict2:

		if key == keys:


			file3.write(">"+key+ "\n"+ dict2[keys]+ " \n")