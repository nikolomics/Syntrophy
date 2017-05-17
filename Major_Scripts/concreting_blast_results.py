#!/usr/bin/python
#Nikolas Strepis 4-2014
#Script for matching the sequences with the database results and then with the fasta file of the database to receive the full names using xml file output from blastp
import os, sys ,fnmatch , numpy, collections

def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)