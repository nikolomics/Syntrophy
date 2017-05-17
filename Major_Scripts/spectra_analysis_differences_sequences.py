#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/analysis_spectra.txt", "r")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/blastp_results/common_proteins_ident_nr.txt")
file3 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/common_proteins_ident_nr.txt", "w")
file4 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/common_accession.txt", "w")
#file4=open("/scratch2/databases/blastdb/UniProt/SwissProt/uniprot_sprot.fasta")
dict1={}
dict2={}
dict3={}
contig1=''
ident =""
accesion=""
dict10={}
for lines in file1:

	contig=lines.strip().split("\t")[0]
	#print contig
	dict1[contig]=lines.strip()

indcat="gamwtokefalimou"
for index, line in enumerate(file2):
	#print line
	
	if "<Iteration_query-def>" in line:
	#	print line
	#	print line 

		contig1 = line.strip().split("def>")[1].split("<")[0]
	#	print contig1
	if "<Hit_num>1<" in line  :
		#print line 
		indcat= int(index) + int(2) 
		inddog= int(index) + int(2)

		#print indcat
		#print contig1
	# get accession numbers	
	if "gt;gi"  in line and index == inddog :

		accesion = line.strip().split("&")[1].split(";")[1].split("|")[0:2]
		accesion = " ".join(accesion)
		dict10[line] = accesion

		print line 
		print [accesion]
	if  "<Hit_def>" in line and index == indcat:
		#print line
		ident=line.strip().split("def>")[1]
		#print contig1,"\t", ident
		
		dict2[contig1] = ident +"\t" + accesion
		#print ident
		#print dict2
#print dict2
#for lina in file4:
	#if ">" in lina:
	#	ide= lina.strip().split("|")[1]
	#	name=lina.strip().split("|")[2]
	#	dict3[ide]=name
#for ko in dict2:
#	idasd =dict2[ko]
#	for kos in dict3:
##		if idasd == kos:
#			dict2[ko] =dict3[kos]


for key in dict1:
	mlk= dict1[key]
	#print mlk
	for keys in dict2:
	#	print keys
		#print key, keys
		if key == keys :
		#	print key,keys
		#	print (dict1[key] + "\t" + dict2[keys] + "\n")
			dict1[key] = mlk +"\t" + dict2[keys]

for ke in dict1:
	#print dict1[ke]

	file3.write(dict1[ke] + "\n")

for ka in dict10:

	file4.write(dict10[ka] + "\n")






