#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys 

file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/analysis_spectra.txt")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/spectra_stereate.xml")
file3 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/common_proteins_seq.txt" , "w")


dict1={}

for index, lines in enumerate(file1):
	#print lines

	contig = lines.strip().split("\t")[0]
	ida = lines.strip().split("\t")[4]
	#print ida


	dict1[contig,ida]=contig
	#print [contig]

dict2={}
seqs=""
contigs=""
for index, lines in enumerate(file2):
	#print line2 
	if '<group id' in lines and 'sumI' in lines :
		idb = lines.strip().split("id")[1].split('"')[1]
		#print idb
		idb = "id=" + idb.replace('"',"")+".1"
		print idb
	if '<note label="description"' in lines :
		contigs = lines.strip().split('">')[1].split("</note")[0]
	#	print contigs
		seq = ""
		#print contig

	if lines.strip().split(" ")[0].isupper():
		#print lines 
		seq += lines.replace("\t","").replace(" ","") 
		#print "sequence" + "\t" + seq
#Here are the sequences retrieved! Nice trick the one that we add the sequence to "" when it finds contig!!
		dict2[contigs,idb] = seq
	#	print dict2
	#print seq
	


for keys in dict1:
	
	#print keys

	for key in dict2:
		#print key, keys
		if keys == key :
			print " hey "

		
		#print dict2[kes]
			file3.write(">"+dict1[key] + "\n" + dict2[keys])









