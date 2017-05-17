#!/usr/bin/python
#CSmall Script to count doimains that u may need from SAAP file 
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

a = sys.argv[1]
file1 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Gen_banks_for_domain_analysis/Galaxy868-[EMBL__LocusTagger__IPR__ORF__Aragorn__FASTA2RDF__S.zehnderi_assemblied_sspace_opera_cap3_scaffold.fasta].embl")
file2 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Genomic_Analysis_S_zehnderi/Hi_seq_analysis/Annotation/Syntrophomonas_zehnderi_SAPP_edit.embl")

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
		dict3[loc]=interall



#print list3

for lines in file2:
	
	if "FT   gene            " in lines:
		

		loc = lines.strip().split("gene")[1].replace(" ","")
		

	if 'FT                   /locus_tag="' in lines:


		name = lines.strip().split('/locus_tag="')[1].replace('"',"")

		dict2[loc]=name




info=[]
info2=[]
indo=[]
a = str(a)
for key in dict1:

	if a in dict1[key]:
		

	#	print key, dict1[key].count("IPR009075")



		info =info + [key + "("+str(dict1[key].count(a))+")"] 
		


print ",".join(sorted(info))
hey =[]

for key in dict3:

	if a in dict3[key]:


		list3=list3+[key]

for key in dict2:
	
	if key in list3 or key.split("..")[0] in list3 or key.split("..")[1] in list3 or key.replace(">","") in list3 or key.replace("<","") in list3:

		indo =indo + [dict2[key] + "("+str(list3.count(key))+")"]

print ",".join(sorted(indo))
print len(list3)