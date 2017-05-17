#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for obtaining the spectra hits and the identified proteins for the two spereated conditions . It has to be ran in twice (for oleate and steraeate) 
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/oleate/oleate_decoy_database/all_oleate_decoy.xml")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/oleate/oleate_decoy_database/info_decoy_oleate_spectra.txt", "w")
dict1 = {}
list1=[]

for index,line in enumerate(file1):

#	if "Andreia" in str(line):
#		name = line.strip().rsplit("/")[0].split("'")[0]
	if "protein expect" in line:
		contig = line.strip().rsplit(">")[0].split("=")[4].split(" ")[0].replace('"',"")
	#	print contig
		info = line.strip().replace('"',"").replace(" ","\t").replace("<","").replace(">","")
		list1+=[contig]

		dict1[info]=contig

	#	print dict1[info]
list2 =[]		
for key in dict1:
	list2+= [dict1[key]]
	#Store all keys/ contigs in a list 
for keys in dict1:
	#If contig is in the list2 then count how many are presnet in the list
	number = list2.count(dict1[keys])
	print number
	if int(number) >= 2:
	#print number
		file2.write(str(dict1[keys]) + "\t" + str(number) +"\t" + str(keys) + "\n") 