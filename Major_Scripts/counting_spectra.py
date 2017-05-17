#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys 



file1 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Proteome_spectra/Proteomics/rawdata/oleate/all.mzXML")
file2 = open ("/home/nstrepis/Syntrophomonas_zehnderi/Proteome_spectra/Proteomics/rawdata/oleate/spectra_peaks.txt", "w")

indexa =0

for index, lines in enumerate(file1):

	if 'precision="32"></peaks>' in lines :
		indexa = int(index) +1 
		print indexa

	#if '</scan><scan' in int(indexa) ==int(index):
	#	a = "nikolas"

	else:

		file2.write(lines)
