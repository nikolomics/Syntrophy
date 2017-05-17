#!/usr/bin/python
#CSmall Script to count doimains that u may need from SAAP file 
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


a = "Swol_0788"
file1 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Gen_banks_for_domain_analysis/Galaxy770-[EMBL__LocusTagger__Annotation__IPR__ORF__CRISPR__Aragorn__FASTA2RDF__wolfei_genome.fasta].embl")
file2= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/S_wolfei_cds.txt")

dict1={}
dict2={}
list3=[]
dict3={}
for index, lines in enumerate(file1):


	if 'FT   gene            ' in lines:

		loc = lines.strip().split('FT   gene            ')[1]

		

	if "FT                   /locus_tag=" in lines:


		gene = lines.strip().split('locus_tag="')[1].replace('"',"")

		interall =""
		seq = ""
	if '/db_xref="InterPro:' in lines:

		inter = lines.strip().split("InterPro:")[1] 
		interall = interall + inter
		#print interall
		dict1[gene]=interall
		dict3[loc]=gene

#print dict1

#print list3

for lines in file2:

	if ">" in lines:
		#print lines
		if "(" in  lines.strip().split(" ")[-1] in lines :
			loc = lines.strip().split(" ")[-1].split("=")[1].replace("]","").replace(">","").replace("<","")
			name = lines.strip().split(" ")[1].split("=")[1].replace("]","")
			dict2[loc]=name
	#		loc = lines.strip().split("gene")[1].replace(" ","")
		else:
			loc = lines.strip().split(" ")[-1].split("=")[1].replace("]","").replace(">","").replace("<","")
		
			name = lines.strip().split(" ")[1].split("=")[1].replace("]","")
			dict2[loc]=name




a= a.split(",")
whop=""
for i in a:
    i=i.replace(" ","")
    i=str(i)
    print i
    for key in dict2:
    	if dict2[key] ==i:
			for keys in dict3:

				if key==keys or key.split("..")[1] in keys or key.split("..")[0] in keys:
					magic = dict1[dict3[keys]].count("IPR")

					print dict1[dict3[keys]].replace('"'," ")
					whop=whop + "|" + dict1[dict3[keys]].replace('"'," ") 
				#print dict1[dict3[keys]].replace('"'," "), "\n",  magic


                   #print dict1[dict3[keys]].replace('"'," ") 
                    

print whop


b=whop.split("|")
numb =""

for i in b:

    i=i.count("IPR")
    numb =numb + "|" + str(i)

print numb