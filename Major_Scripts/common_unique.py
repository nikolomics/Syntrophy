#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


file1=open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/oleate/export_Example.txt")
file2=open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/stearate/exported_proteins.txt")
file3= open("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/common_proteins.txt", "w")
file4 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/unique_proteins_oleate.txt", "w")
file5 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Peptide_Shaker/unique_proteins_stearate.txt", "w")


dict1={}
dict2={}

list1=[]
list2=[]
for index, lines in enumerate(file1):
	protein = lines.strip().split("\t")[0]
	list1= [protein] + list1
	#print [protein]
	dict1[protein]= protein


for index, lines in enumerate(file2):

	protein = lines.strip().split("\t")[0]
	list2=[protein]+ list2	
	#print [protein]

	dict2[protein]=protein

list3=[]

for key in dict1:
	for keys in dict2:


		if key == keys:
			list3=[key] + list3
			#print len(list3)
		#	print key +"\n"

			file3.write(key + "\n")

file3.close

#print list3

for key in dict1:
#	print [key] , "list" , list3
	if key not in list3:
		print "hello", key
		file4.write(key +"\n")
file4.close
for key in dict2:

	if key not in list3:


		file5.write(key + "\n")

file5.close