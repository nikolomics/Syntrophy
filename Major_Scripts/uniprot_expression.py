#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1=open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/zehnderi_oleate_id_expression.csv")

file2= open ("/Users/NikolasStrepis/Desktop/uniprot-yourlist%3AM2014120513FOZC0L7V.tab")

file3 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/differential_expression_oleate_zehnderi_uni_prot.csv", "w")


dict1={}


dict2={}


list2=[]
list3=[]

for index, lines in enumerate(file1):

	contig= lines.strip().split("\t")[2].split("|")[1]
	#print contig 
	info=lines.strip()


	dict1[contig]=info
	list2=[contig] + list2

for index, lines in enumerate(file2):




	contig = lines.strip().split("\t")[24]


	info = lines.strip()

	#print lines

	dict2[contig]=info

	list3=[contig]+list3
list1=[]
list5=[]
for key in dict1:

	for keys in dict2:
		print [key], [keys]

		
		if key in keys:
			list1=[key]+list1
			#print dict1[key] + "\t" + dict2[keys] + "\n"
			file3.write(dict1[key] + "\t" + dict2[keys] + "\n")
for key in dict1:


	if key not in list1:

		list5=list5+[key]

print list5
print len(list5)

print "done"

	
print len(list2)
print len(list3)
print len(list1)

file3.close





