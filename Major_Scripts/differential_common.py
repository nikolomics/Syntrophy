#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1=open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/common_match.txt")
file2= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/oleate/export_Example.txt")
file3=open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/stearate/exported_proteins.txt")
file4 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/differential_common.txt","w")


dict1={}
dict2={}
dict3={}

for index,lines in enumerate(file1):

	contig = lines.strip().split("\t")[0]
	#print contig
	sente = lines.strip()

	dict1[contig] = sente


for index, lines in enumerate(file2):

	contig = lines.strip().split("\t")[0]
#	print contig
	peptides = lines.strip().split("\t")[6]
	#print peptides

	dict2[contig] = peptides


for index, lines in enumerate(file3):
	contig = lines.strip().split("\t")[0]
	#print contig
	peptides = lines.strip().split("\t")[6]


	dict3[contig] = peptides


dict4={}
for key in dict2:

	for keys in dict3:

		if key == keys:
			dict4[key] = dict2[key] + "\t" + dict3[key]


for key in dict1:

	for keys in dict4:


		if key == keys:


			print dict1[key] + "\t" + dict4[keys]

			file4.write(key+"\t" + dict4[keys] + "\t" + dict1[key] +"\n")



file4.close		



