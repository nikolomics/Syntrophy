#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for obtaining the one hit proteins that do not have match anywhere in the spectra. It can be used and for noraml reiciving of the proteiones (it must be run twice)
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1 = open("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/spectra_stereate.xml")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/info_stereate_spectra_one_hit.txt", "w")
file3 = open("/home/nstrepis/Syntrophomonas_zehnderi/Tools/tandem-linux-13-07-22-1/bin/64-bit/all_static/stereate/decoy_database/all_decoy_stereate.xml")
dict1 = {}
list1=[]
dict2 ={}
dict4={}
contig=""
info=""
list01=[]
sequence=""
peptide=""
percen=""
for index,line in enumerate(file1):
	#print [line]
#	if "Andreia" in str(line):
#		name = line.strip().rsplit("/")[0].split("'")[0]
	if "protein expect" in line:
		contig = line.strip().rsplit(">")[0].split("=")[4].split(" ")[0].replace('"',"")
	#	print contig
		info = line.strip().replace('"',"").replace(" ","\t").replace("<","").replace(">","")
		list1+=[contig]
	if "seq=" in  line and "pre" in line :
		
		sequence= line.strip().rsplit(" ")[15].split("=")[1].replace('"',"")
		#print sequence

		

		dict1[info]=contig,sequence

	
for wookie in file3:
	if "seq="in wookie and "pre" in wookie:
		peptide = wookie.strip().rsplit(" ")[15].split("=")[1].replace('"',"")
		#print peptde
		dict4[peptide]=peptide
for woo in dict4:
	#print [woo]
	list01 += [woo]
	#print list01
	#	print dict1[info]
dict5={}	
list2 =[]		
for key in dict1:
	#print dict1[key]
	cont, seq = dict1[key]
	dict5[cont]=key,seq
	#print cont, seq
	list2+= [cont]
	list1+=[seq]
#	print list1
	#Store all keys/ contigs in a list 
for keys in dict5:
	#print dict5[keys]
	info,seq1=dict5[keys]
	
	#If contig is in the list2 then count how many time it is and report back
	number = list2.count(keys)
	number2=list1.count(seq1)
	print number2
	number3=list01.count(seq1)
	#print number3
	if int(number) != 0 and int(number3) !=0:
		print"hello"
		percen = (int(number) /  int(number3) ) * 100 + "%"
		print percen
	#print number
	if int(number) >= 2 :
	
	#print number
		file2.write(keys+ "\t" + str(number) +"\t" + str(info) + "\t" + percen + "\n") 
	# In thus point the script can become as the spectra_analysis and s tore only the ones that have peptides more than 2
	if int(number) ==1 and int(number2)==1:
		
		file2.write(keys + "\t" + str(number) +"\t" + str(info) + "\t"+ "unique_peptide" + "\t" + percen + "\n" )





