#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/unique_proteins_stearate.txt")
file2 = open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/M.formicicum_naive_translation.fasta")
file3 = open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/M.formicicum_naive_stearate_proteins.fasta" , "w")

#head = file1.readlines()

dict1={}
dict2={}
for index, lines in enumerate(file1):
	#print lines
	contig=lines.strip().split("\t")[0]

	dict1[contig]=contig
	#print [contig]


for index, lines in enumerate(file2):

	if ">" in lines:
		contig = lines.strip().split(" ")[0].replace(">","")
		seq=""
		#print [contig]
	else:
		seq = seq+lines
		dict2[contig]=seq

for key in dict1:
	#print key

	for keys in dict2:
	
		if key == keys:

		#	print ">" + dict1[key] + "\n" + dict2[keys] 
			file3.write(">" + dict1[key] + "\n" + dict2[keys] )





file3.close