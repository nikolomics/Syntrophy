#!/usr/bin/python
#domain core trichococcus
import os, sys ,fnmatch , numpy, xlrd

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)



file1= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/syntrophomonas_all_domains.csv")
file2= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/syntrophomonas_zehnderi_domains.csv", "w")
file3= open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/syntrophomonas_wolfei_domains.csv", "w")
file4=open ("/Users/NikolasStrepis/Documents/PhD_Projects/S.zehnderi_unsaturated/Genomic_analysis/syntrophomonas_wolfei_methyl_domains.csv", "w")



for lines in file1:
	info1=int(lines.strip().split(";")[2])
	info2=int(lines.strip().split(";")[3])
	info3=int(lines.strip().split(";")[4])

	if info1 >0 and info2==0 and info3==0:

		file2.write(lines)

	if info1==0 and info2>0 and info3 ==0:
		file3.write(lines)

	if info1==0 and info2 ==0 and info3>0:
		file4.write(lines)