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
dict8={}
dict9={}


dict10={}
dict11={}

dict111={}
dict222={}
dict333={}

dict555={}
dict666={}
dict777={}

dict888={}

list11=[]
list22=[]
list33=[]
list111=[]
list222=[]
list333=[]
for lines in file1:


	query = lines.strip().split("\t")[0]

	match = lines.strip().split("\t")[1]

	ident = lines.strip().split("\t")[2]

	if "ref" in query:

	  	
		if query in dict7:
			dict7[query].append(ident)
		else:

			dict7[query] = [ident]

	if "dbj" in query :
		if query in dict10:
			dict10[query].append(ident)
		else:

			dict10[query] = [ident]

	if "scaffold" in query or "Contig" in query:
			
		if query in dict11:

			dict11[query].append(ident)
		else:

			dict11[query] = [ident]

	if float(ident) != 100 :

		if "ref" in query:

			list11+=[query]
			if query in dict1:
				dict1[query].append(ident)
			else:

				dict1[query] = [ident]


		if "scaffold" in query or "Contig" in query:
			list22+=[query]
			if query in dict2:
				dict2[query].append(ident)
			else:

				dict2[query] = [ident]


		if "dbj" in query :
			list33+=[query]
			if query in dict3:
				dict3[query].append(ident)
			else:

				dict3[query] = [ident]


		if "ref" in query and "dbj" not in lines:
			if query in dict5:
				dict5[query].append(ident)
			else:

				dict5[query] = [ident]


		if "ref" in query and "scaffold" not in lines or "Contig" not in lines:

			if query in dict6:
				dict6[query].append(ident)
			else:

				dict6[query] = [ident]
		if "dbj" in query and "ref" not in lines :
			if query in dict8:
				dict8[query].append(ident)
			else:

				dict8[query] = [ident]


#common proteins

		if "ref" in query and "scaffold" in lines or "Contig" in lines and "dbj" not in lines:

			if query in dict111:
				dict111[query].append(ident)
			else:

				dict111[query] = [ident]

		if "ref" in query and "dbj" in lines and "scaffold" not in lines or "Contig" not in lines:
			if query in dict222:
				dict222[query].append(ident)
			else:
				dict222[query] = [ident]

		if "dbj" in query and "scaffold" in lines or "Contig" in lines and "ref" not in lines:
			if query in dict333:
				dict333[query].append(ident)
			else:
				dict333[query] = [ident]

		if "dbj" in query and "scaffold" in lines or "Contig" in lines and "ref" in lines:
			if query in dict888:
				dict888[query].append(ident)
			else:
				dict888[query]=[ident]



#total proteins for some reason they are more

	else:
		if "ref" in query:
			list111+=[query]
		if "dbj" in query:
			list222+=[query]
		if "scaffold" in lines or "Contig" in query:
			list333 +=[query]

print len(list111), len(list222), len(list333)

for key in dict7:

	if len(dict7[key]) ==1:
		print "wolfei", key

for key in dict10:

	if len(dict10[key]) ==1:
		print "methy", key

for key in dict11:
	if len(dict11[key])==1:
		print "zehnderi", key


list1=[]
list2=[]
list3=[]
list5=[]
list6=[]
list8=[]
list9=[]
list10=[]
list11=[]
list12=[]
#print dict3

for key in dict1:
	

	if all(float(i) <= 35 for i in dict1[key]):
	#	print dict1[key]

		list1=[key] + list1
		file2.write(key + ";" + ";".join(dict1[key]) +"\n")


for key in dict2:
	if all(float(i) <= 35 for i in dict2[key]):


		list2=[key] + list2
		file3.write(key + ";" + ";".join(dict2[key]) +"\n")



for key in dict3:
	if all(float(i) <= 35 for i in dict3[key]):


		list3=[key] + list3
		file4.write(key + ";" + ";".join(dict3[key]) +"\n")
print len(list1), len(list2), len(list3)

#unique per two couples
for key in dict5:
	if all(float(i) <= 35 for i in dict5[key]):
	#	print dict5[key]

		list5=[key] + list5
print len(list5)

for key in dict6:
	if all(float(i) <= 35 for i in dict6[key]):
	#	print dict5[key]

		list6=[key] + list6
print len(list6)

for key in dict8:
	if all(float(i) <= 35 for i in dict8[key]):
	#	print dict5[key]

		list8=[key] + list8
print len(list8)

#common proteins
for key in dict111:
	if all(float(i) >= 35 for i in dict111[key]):
	#	print dict5[key]

		list9=[key] + list9
print len(list9)


for key in dict222:
	if all(float(i) >= 35 for i in dict222[key]):
	#	print dict5[key]

		list10=[key] + list10
print len(list10)

for key in dict333:
	if all(float(i) >= 35 for i in dict333[key]):
	#	print dict5[key]

		list11=[key] + list11
print len(list11) 

for key in dict888:
	if  all(float(i) >= 35 for i in dict888[key]):

		list12=[key] + list12
print len(list12)
#for common proteins

