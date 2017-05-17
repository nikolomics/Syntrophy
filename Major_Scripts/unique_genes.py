#!/usr/bin/python
#Match fast headers with ammino acids

import os, sys ,fnmatch , numpy, xlrd


file1=open( "/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/roary_annotation_comparison_of_the_genomes/gene_presence_absence.csv")




list1=[]
list2=[]
list3=[]


list4=[]
list5=[]
list6=[]
for lines in file1:


	if "mehtylbutirica" not in lines and "wolfei" not in lines:

	
		list1= list1+[lines]


	if "zehnderi_good" not in lines and "mehtylbutirica" not in lines:
		
		list2=list2+[lines]

	if "zehnderi_good" not in lines and "wolfei" not in lines:

		list3=list3 + [lines]

	if "zehnderi_good" in lines and "wolfei" in lines and "mehtylbutirica" not in lines:
		print lines
		list4=list4 + [lines]


	if "zehnderi_good" in lines and "wolfei"  not in lines and "mehtylbutirica" in lines:

		list5+=[lines]

	if "zehnderi_good" not in lines and "wolfei"  not in lines and "mehtylbutirica" in lines:

		list6+=[lines]

#zehnderi unqiue
print len(list1)


#wolfei unique
print len(list2)

#methybutirica
print len(list3)

print "\n"
#common zehnderi and wolfei

print len(list4) + 1320

#common zehnderi and methybutirica

print len(list5) + 1320

#common methbyutrica and wolfei


print len(list6) + 1320