#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)





file1= open ("/home/nstrepis/Genomic_comparison/mergedblastp/first_colum_zehnderi_unique.txt")
file2= open("/home/nstrepis/Genomic_comparison/Proteins/S.zhenderi_translated_proteins.fasta")
file3= open("/home/nstrepis/Genomic_comparison/unique_sequences_zehnderi.fasta" ,"w")

seq=""
contig=""



dict1={}
dict2={}


for index, lines in enumerate(file1):

	contig = lines.strip()

	dict1[contig] = contig


for index, lines in enumerate(file2):

	if ">contig" in lines :


		contig = lines.strip().split("#")[0].replace(">","").replace(" ","")
		seq=""
		print contig

	else:

		seq = seq+lines

		dict2[contig]=seq

#print dict2

for key in dict1:
	for keys in dict2:
		#print [key], [keys]
		if key == keys:
			print "hello"
			file3.write(">" + keys + "\n" + dict2[keys] )


