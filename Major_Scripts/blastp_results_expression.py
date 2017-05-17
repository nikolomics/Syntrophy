#!/usr/bin/python
#Nikolas Strepis 4-2014
#Best script for blast matches it can use the general form and take the best hit!!
import os, sys ,fnmatch , numpy

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open("/home/nstrepis/S.zehnderi/blastp/stearate_s.zhenderi_blastp.txt" )
file2 = open ("/home/nstrepis/S.zehnderi/blastp/expression/info_stereate_spectra_one_hit.txt")
file3 = open("/home/nstrepis/S.zehnderi/blastp/expression/zehnderi_stearate_id_expression.csv", "w")

dict1={}
dict2={}
indexa=""
hit ="nikos"
list1 =[]
list2 = []
list3=[]
indexb=""
hit2="nikos"
for index, lines in enumerate(file1):

	if "Query= " in lines:

		#print lines
		contig = lines.strip().split(" ")[1]
		indexa = index + 6
		hit ="nikoa"
		protein =""
		list1= [contig] + list1
	if index == indexa and "|" in lines:
		#print lines

		hit = lines.strip().split("...")[0].split("]")[0].split("|")[2]
	 	#print hit
		hit2 = lines.strip().split("...")[0].split("]")[0].split("|")[1]
		list2= [hit] +list2
		#print lines
		
	if  hit2 in lines  and  ">ref" in lines:
		print [hit2], [hit]
		print lines
		indexb=index + 1
		protein =lines.strip().split(">")[1]


	if index == indexb:
		full_protein = protein + " " + lines.strip()
		#print full_protein
		list3=[protein] + list3
		dict1[contig]= full_protein
		




for index, lines in enumerate(file2):


	contig = lines.strip().split("\t")[0].replace("#","_")


	info = lines.strip().split("\t")[1]


	dict2[contig]=info




for key in dict1:
	#print [key]
	for keys in dict2:
		#print [key], [keys]
		if key == keys :


			#print key + "\t" + dict2[keys] + "\t" + dict1[key] +"\n"
			file3.write(key + "\t" + dict2[keys] + "\t" + dict1[key] +"\n")



print len(list1)

print len(list2)
print len(list3)
file3.close











