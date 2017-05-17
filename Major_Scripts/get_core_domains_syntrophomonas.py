#!/usr/bin/python
#domain core trichococcus
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

file1 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Gen_banks_for_domain_analysis/Galaxy868-[EMBL__LocusTagger__IPR__ORF__Aragorn__FASTA2RDF__S.zehnderi_assemblied_sspace_opera_cap3_scaffold.fasta].embl")
file2 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Gen_banks_for_domain_analysis/Galaxy770-[EMBL__LocusTagger__Annotation__IPR__ORF__CRISPR__Aragorn__FASTA2RDF__wolfei_genome.fasta].embl")
file3 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Gen_banks_for_domain_analysis/Galaxy892-[EMBL__LocusTagger__Annotation__IPR__ORF__Aragorn__FASTA2RDF__Syntrophomonas_wolfei_subsp._methylbutyratica_.fasta].embl")
file4= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/syntrophomonas_all_domains.csv", "w")
file5= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/syntrophomonas_core_domains.csv", "w")
file6=open("/Users/NikolasStrepis/Documents/PhD_Projects/Trichococcus/Interpro_names.txt")


dict1={}
dict2={}
dict3={}
dict4={}
dict5={}
dict6={}
dict7={}
dict8={}



list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]

list11=[]
list21=[]
list31=[]
list41=[]
list51=[]
list61=[]
list71=[]
list81=[]

dictall={}

for lines in file1:


	if '/db_xref="InterPro:' in lines:


		domain = lines.strip().split('/db_xref="InterPro:')[1].replace('"',"")



		list1=list1+ [domain]

		list11=list11+[domain]

		dictall[domain]=domain

for lines in file2:

	if '/db_xref="InterPro:' in lines:


		domain = lines.strip().split('/db_xref="InterPro:')[1].replace('"',"")
		dictall[domain]=domain
		list21 = list21+[domain]
		if domain in list1:

			list2= list2 + [domain]


for lines in file3:

	if '/db_xref="InterPro:' in lines:


		domain = lines.strip().split('/db_xref="InterPro:')[1].replace('"',"")
		dictall[domain]=domain
		list31 = list31+[domain]

		if domain in list2:

			list3=list3 +[domain]

for lines in file6:
	
	if "Active" not in lines:
	
		domains = lines.strip().split("\t")[0]
		name=  lines.strip().split("\t")[1]
	
		dict2[domains]=name

for i in list3:


	dict1[i]=i

list10=[]
for key in dict1:

	for keys in dict2:

		if key == keys:
			list10=list10+[key]
			file5.write(dict1[key] + ";" +  dict2[key] + ";" + str(list1.count(key)) + ";" + str(list2.count(key)) + ";" + str(list3.count(key))+  "\n")

for key in dict1:


	if key not in list10:
		file5.write(dict1[key] + ";" +";" + str(list1.count(key)) + ";" + str(list2.count(key)) + ";" + str(list3.count(key))+ "\n")


listall=[]
for key in dictall:
	for keys in dict2:

		if key ==keys:
			listall=[]
			file4.write(key + ";" + dict2[key] +";"+  str(list11.count(key)) + ";" + str(list21.count(key)) + ";" + str(list31.count(key))+  "\n")

		#	print (key + ";" + dict2[key] +  str(list11.count(key)) + ";" + str(list21.count(key)) + ";" + str(list31.count(key))+ ";"+ str(list41.count(key)) + ";" + str(list51.count(key)) + ";" + str(list61.count(key)) + ";"+ str(list71.count(key))+ "\n")
for key in dictall:
	if key in listall:
		file4.write(key + ";" + ";" +  str(list11.count(key)) + ";" + str(list21.count(key)) + ";" + str(list31.count(key))+ "\n")


file4.close()

