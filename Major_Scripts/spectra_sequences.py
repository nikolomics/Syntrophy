#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys 



file1 = open("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/oleate/spectra_oleate.xml")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/spectra_stereate.xml")
file3 = open("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/oleate/spectra_sequences_oleate.fasta" , "w")
file4 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/spectra_sequences_sterate.fasta", "w")

dict1={}
dict2={}
seq=""
contig=""
contigs=""
seqs=""
for index, line in enumerate(file1):
	#print line 
	if '<note label="description"' in line :
		contig = line.strip().split('">')[1].split("</note")[0].replace("#","_")
		print [contig]
		seqs="" 

	if line.strip().split(" ")[0].isupper():
		#print [line.replace("\t","").replace(" ","")]
		seqs += line.replace("\t","").replace(" ","") 
		#print seqs
	
		dict1[contig] = seqs
		
	


for index, lines in enumerate(file2):
	#print line2 
	if '<note label="description"' in lines :
		contigs = lines.strip().split('">')[1].split("</note")[0].replace("#","_")
		seq = ""
		#print contig

	if lines.strip().split(" ")[0].isupper():
		#print lines 
		seq += lines.replace("\t","").replace(" ","") 
		#print "sequence" + "\t" + seq
#Here are the sequences retrieved! Nice trick the one that we add the sequence to "" when it finds contig!!
		dict2[contigs] = seq
	#print seq
	


for key in dict1:

	file3.write(">" + key + "\n" + dict1[key])


for key in dict2 :
	#print dict2[key] + "\n" 
	file4.write(">" + key + "\n" + dict2[key])
