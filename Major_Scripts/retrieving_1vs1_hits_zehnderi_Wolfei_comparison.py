#!/usr/bin/python
#Script for retrieving sequences after seperating common 1vs1 hits for wolfei comparison.

import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/Gene_Comparison/1vs1_hits_srv35.txt")
file2=open("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/S.zehnderi_prodigal_sspace_proteins.fasta")
file3 = open ("/home/nstrepis/Syntrophomonas_zehnderi/syntrophomonas_zehnderi_wolfei_comparison/Gene_Comparison/common_1vs1_sequences.fasta", "w")


dict1={}
dict2={}
list1=[]
list2=[]
for index,lines in enumerate(file1):


	query = lines.strip().split("\t")[2]
	info = lines.strip()
	#print query
	list1=list1+[query]

	dict1[info]=query


for index, lines in enumerate(file2):



	if ">" in lines :

		query = lines.strip().split("#")[0].replace(" ","").replace(">","")
		#print query
		seq = ""

	else:


		sequence = lines.strip()
		#print sequence
		seq = str(sequence) + seq

		dict2[query]= sequence

key=""
for aloha in dict1:
	key=dict1[aloha]
	list2=[aloha]+ list2
	for keys in dict2:

		if key == keys:


			file3.write(">"+key+ "\t" + aloha + "\n"+ dict2[keys]+ " \n")


print len(list2)