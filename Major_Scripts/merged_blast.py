#!/usr/bin/python
#domain core trichococcus
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)


file1=  open ("/Users/NikolasStrepis/Documents/PhD_Projects/Genomic_comparison_zehnderi_wolfei/merged_3_results.txt")

file2=  open ("/Users/NikolasStrepis/Documents/PhD_Projects/Genomic_comparison_zehnderi_wolfei/unique_wolfei.csv" , "w")

file3= open ("/Users/NikolasStrepis/Documents/PhD_Projects/Genomic_comparison_zehnderi_wolfei/unique_zehnderi.csv" , "w")

file4= open ("/Users/NikolasStrepis/Documents/PhD_Projects/Genomic_comparison_zehnderi_wolfei/unique_methylbutyrica.csv" , "w")


dict1={}
dict2={}
dict3={}

dict5={}
dict6={}
dict7={}

list11=[]
list22=[]
list33=[]
for lines in file1:


	query = lines.strip().split("\t")[0]

	match = lines.strip().split("\t")[1]

	ident = lines.strip().split("\t")[2]


	if float(ident) > 35 :

		if "ref" in query:

			list11+=[query]
			if query in dict1:
				dict1[query].append(lines.strip())
			else:

				dict1[query] = [lines.strip()]
	else:

		if "ref" in query and query not in list11:

			
			if query in dict5:
				dict5[query].append(lines.strip())
			else:

				dict5[query] = [lines.strip()]

	if float(ident) > 35 :

		if "scaffold" in query or "Contig" in query:
			list22+=[query]
			if query in dict2:
				dict2[query].append(lines.strip())
			else:

				dict2[query] = [lines.strip()]
	else:
		if "scaffold" in query or "Contig"in query and query not in list22:

			
			if query in dict6:
				dict6[query].append(lines.strip())
			else:

				dict6[query] = [lines.strip()]

			



	if float(ident) > 35 :

		if "dbj" in query :
			list33+=[query]
			if query in dict3:
				dict3[query].append(lines.strip())
			else:

				dict3[query] = [lines.strip()]
	else:

		if "dbj" in query and query not in list33 :

			if query in dict7:
				dict7[query].append(lines.strip())
			else:

				dict7[query] = [lines.strip()]

list1=[]

list2=[]

list3=[]

print dict3

#for key in dict1:
	#if len(dict1[key])==1:	
	#	list1=[key] + list1
	#	file2.write(";".join(dict1[key]) +"\n")

for key in dict5:
	list1=[key] + list1
	file2.write(";".join(dict5[key]) +"\n")

#for key in dict2:
#	if len(dict2[key])==1:
#		list2=[key] + list2
#		file3.write(";".join(dict2[key]) +"\n")

#for key in dict6:
	list2=[key] + list2
	file3.write(";".join(dict6[key]) +"\n")


#for key in dict3:


#	if len(dict3[key])==1:
#		list3=[key] + list3
#		file4.write(";".join(dict3[key]) +"\n")

for key in dict6:
	list3=[key] + list3
	file4.write(";".join(dict6[key]) +"\n")


print len(list1), len(list2), len(list3)
