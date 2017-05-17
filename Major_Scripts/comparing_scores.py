#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)




file1= open("/home/nstrepis/Genomic_comparison/tblastn_unique_sequences_zehnderi.fasta")
file2 = open ("/home/nstrepis/Genomic_comparison/tblastn_unique_sequences_zehnderi_scores_evaluated.fasta", "w")



for index, lines in enumerate(file1):

	
	scorea= lines.strip().split("\t")[2].split(" ")[2]
	#print lines.strip().split("\t")[2].split(" ")
	if scorea !='':
		scorea = lines.strip().split("\t")[2].split(" ")[2]
	else:
		scorea =lines.strip().split("\t")[2].split(" ")[3]
	scoreb = lines.strip().split("\t")[4]
	#print scorea


	if float(scorea) <  0.35 * float(scoreb) :
		print float(scorea),  0.35 * float(scoreb), scorea, scoreb
		print "hello"

		file2.write(lines)






