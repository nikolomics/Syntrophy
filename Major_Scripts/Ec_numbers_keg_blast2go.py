#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys 


file1 = open("/Users/NikolasStrepis/Desktop/keg_oleate/kegg_txt_20140617_1300.txt") 

file2 = open("/Users/NikolasStrepis/Desktop/keg_oleate/EC_numbers.txt", "w")

file1.readline()
for lines in file1:

	EC = lines.strip().split("\t")[3].replace(":","").replace("ec","E")


	file2.write(EC + "\n")

