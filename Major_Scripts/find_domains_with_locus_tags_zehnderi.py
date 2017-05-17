#!/usr/bin/python
#CSmall Script to count doimains that u may need from SAAP file
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)

a = "2006"
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
        dict3[loc]=gene

#print dict1

#print list3

for lines in file2:

    if "FT   gene            " in lines:

        loc = lines.strip().split("gene")[1].replace(" ","")

    if 'FT                   /locus_tag="' in lines:

        name = lines.strip().split('/locus_tag="')[1].replace('"',"")

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

               if key==keys:
                   magic = dict1[dict3[keys]].count("IPR")

                   #print dict1[dict3[keys]].replace('"'," "), "\n",  magic
                   print dict1[dict3[keys]].replace('"'," ") 
                   whop=whop + "|" + dict1[dict3[keys]].replace('"'," ") 

print "\n"
print whop


b=whop.split("|")
numb =""
print b
for i in b:

    i=i.count("IPR")
    numb =numb + "|" + str(i)

print numb