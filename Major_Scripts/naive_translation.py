#!/usr/bin/python
#Nikolas Strepis 4-2014 - Jasperk
#Naive translateion. 
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
from Bio import SeqIO
import sys

def main():
    input = sys.argv[1]
    for seq_record in SeqIO.parse(input, "fasta"):
        translation(Seq(str(seq_record.seq)),1,"FWD_1_"+str(seq_record.id))
        translation(Seq(str(seq_record.seq)[1:]),1,"FWD_2_"+str(seq_record.id))
        translation(Seq(str(seq_record.seq)[2:]),1,"FWD_3_"+str(seq_record.id))

        translation(Seq(str(seq_record.seq)).reverse_complement(),1,"REV_1_"+str(seq_record.id))
        translation(Seq(str(seq_record.seq)[:-1]).reverse_complement(),1,"REV_2_"+str(seq_record.id))
        translation(Seq(str(seq_record.seq)[:-2]).reverse_complement(),1,"REV_3_"+str(seq_record.id))
    print ("done")
    
def translation(seq,codon,header=""):
    print (header, seq[:10])
    AAsequence = seq.translate(table=codon)
    output = open(sys.argv[1]+".output","a")
    for index, AA in enumerate(AAsequence.split("*")):
        if len(AA) > 0:
            output.write(">"+str(header)+"#"+str(index)+"\n"+str(AA)+"\n")

if __name__ == '__main__':
    main()