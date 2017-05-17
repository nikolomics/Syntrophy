#!/usr/bin/python
#Great Script to find domains in zehnderi depending on the gene input number (locus tag) and in S wolfei
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

#a = sys.argv[1]
file1 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Genomic_Analysis_S_zehnderi/Hi_seq_analysis/Annotation/Syntrophomonas_zehnderi_SAPP_edit.embl")
file2 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/Galaxy399-[EMBL__PRIAM__SWISSCOG__Annotation__IPR__TMHMM__signalP__RNA__ORF__CRISPR__FASTA2RDF__Syntrophomonas_wolfei_Goettingen_uid58179].embl")
file3= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/S_wolfei_copy.txt")
file4 = open("/Users/NikolasStrepis/Documents/PhD_Projects/Genomic_comparison_zehnderi_wolfei/Tables_for_manuscript/Tables_for_enzymes.csv")
file5 = open ("/Users/NikolasStrepis/Documents/PhD_Projects/Genomic_comparison_zehnderi_wolfei/Tables_for_manuscript/FA_degradation_domains.csv" , "w")




dict1={}
dict2={}
dict8={}
dict3={}
inter=""
gene=""
indexa=""


for index, lines in enumerate(file1):


	if "FT                   /locus_tag=" in lines:

		indexa=index +1


		gene = lines.strip().split('locus_tag="')[1].replace('"',"")
		#print gene
		interall =""
		seq = ""



	if "FT                   /product=" in lines and  indexa==index:
	

		name= lines.strip().split("/product")[1].replace('"',"").replace("=","")


		dict1[gene]=[name]

	if 'FT                   /inference="protein motif:InterPro' in lines:
		inter = lines.strip().split("InterPro:")[1].replace('"',"") 
		if inter in dict1:
	#	print func
			
			dict1[inter].append(gene)
			#print dict1[gene]
		else:

			dict1[inter]= [gene]


for index, lines in enumerate(file2):


	if 'FT   gene            ' in lines:

		loc = lines.strip().split('FT   gene            ')[1]

		

	if "FT                   /locus_tag=" in lines:


		gene = lines.strip().split('locus_tag="')[1].replace('"',"")

		interall =""
		seq = ""
	if '/db_xref="InterPro:' in lines:

		inter = lines.strip().split("InterPro:")[1].replace('"',"") 



		if inter in dict2:
	#	print func
			
			dict2[inter].append(loc)
			#print dict1[gene]
		else:

			dict2[inter]= [loc]
		

for lines in file3:

	if "     gene            " in lines:
		#print lines

		gene = lines.strip().split("gene")[1].replace(" ","")
		

	if '                     /locus_tag="' in lines:


		loc = lines.strip().split('/locus_tag="')[1].replace('"',"")

		dict8[gene]=loc





list3=[]

info=[]
info2=[]
dict3={}
dict4={}
list4=[]
list5=[]
okie =""
ok=""
for index, lines in enumerate(file4):

	if "Locus" not in lines:

		here= lines.strip().split(";")[4].split(",")

		list5= list5 + here
		

		herea= lines.strip().split(";")[6].split(",")
		list4=list4+herea


dict6={}
for key in dict1:
	for i in dict1[key]:
		
		for asd in list5:
			

			if i == no:
				

				okie = key +";" + ",".join(dict1[key]) +";"
				dict6[key]=[okie]

#correct so far


list7=[]

#print dict6
for key in dict2:
	qw=dict2[key]
	for i in qw:
		if i in dict8:
				
			if key in dict4:
	#	print func
				
				dict4[key].append(dict8[i])
			#print dict1[gene]
			else:

				dict4[key]= [dict8[i]]




for key in dict4:

	lets=dict4[key]



	
	for i in lets:
		#print i
		for asd in list4:

			if i == asd:
				
				if key in dict6:
					hoi = ";" + ",".join(dict4[key])
					hoi =hoi

					print dict6[key]
	#	print func

					dict6[key].append(hoi)
			#print dict1[gene]
				else:


					dict6[key]= [hoi]


				

for key in dict6:
	print dict6[key]


	file5.write(key + ";" + ",".join(dict6[key]) + "\n")



file5.close()



