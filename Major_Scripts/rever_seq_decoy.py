#!/usr/bin/python
#Nikolas Strepis 4-2014
#Create decoy database 
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


file1 = open("/home/nstrepis/Syntrophomonas_zehnderi/S.zehderi_Merged1_noscaffold_e/454S.zehderi_seq.fasta.output")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/S.zehderi_Merged1_noscaffold_e/454S.zehderi_seq_reverse.fasta", "w")
rev_seq=""
dict1 ={}
for lines in file1:

	if ">" in lines:
		contig=lines.strip()

	else:
		sequence =lines.strip().split()
		#print sequence
		rev_seq= lines.strip()[::-1]
		#print rev_seq

	dict1[contig]=rev_seq

for key in dict1:

	file2.write( key+ "\n" + dict1[key] +"\n")


