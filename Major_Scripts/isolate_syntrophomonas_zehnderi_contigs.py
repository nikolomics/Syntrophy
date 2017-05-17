#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open("/home/nstrepis/Syntrophomonas_zehnderi/Assemblies/S.zehderi_Merged1_noscaffold_e/S.zehnderi_contigs.txt")
file2 = open("/home/nstrepis/Syntrophomonas_zehnderi/Assemblies/S.zehderi_Merged1_noscaffold_e/454LargeContigs.fna")
file3 = open("/home/nstrepis/Syntrophomonas_zehnderi/Assemblies/S.zehderi_Merged1_noscaffold_e/S.zehnderi_sequences.txt" , "w")


dict1={}
dict2={}
for index, lines in enumerate(file1):
	
	contig=lines.strip().split("\t")[1]

	dict1[contig]=contig
#	print [contig]


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

			print ">" + dict1[key] + "\n" + dict2[keys] 
			file3.write(">" + dict1[key] + "\n" + dict2[keys] )





file3.close