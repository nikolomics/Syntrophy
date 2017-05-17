#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for finding the different proteins for the two different conditions and counting the peptides 
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/info_stereate_spectra_one_hit.txt", "r")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/oleate/info_oleate_spectra_one_hit.txt", "r")
file3 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/analysis_spectra.txt", "w")

dict1={}
dict2={}
for lines in file1:

	contig = lines.strip().split("\t")[0]
	dict1[contig]=lines.strip()

for line in file2:

	contig1=line.strip().split("\t")[0]
	dict2[contig1]=line.strip().split("\t")[1:]
#	print contig

for key in dict1:
	
	for keys in dict2:
		#print key, "\t", keys
		if key == keys:
			#print keys
			file3.write(str(dict1[key])+"\t" + "\t".join(dict2[key]) +"\n")



