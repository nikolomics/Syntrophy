###needs -outfmt7
sBasePath = "/home/bastian/Data/other_organisms/coline_clostridia/dakarense/"
sInputFile = "FINAL_AUTOMATIC_dakarense_ANNOTATION.gbk.3.embl_protein_multifasta_vs_themself.selftest.blastresult"
inputFile = open(sBasePath+sInputFile,"r")
outputFile = open(sBasePath+sInputFile+"_more_than_1_hit.new.txt","w")
outputFile2 = open(sBasePath+sInputFile+"_more_than_1_hit_60-95%.new.txt","w")
outputFile3 = open(sBasePath+sInputFile+"_more_than_1_hit_80-95%.new.txt","w")
sQuery = ""

for lines in inputFile.xreadlines():
    if lines[0]=="#":continue

          
    lStuff = lines.split("\t")

    iIdent = float(lStuff[2])
    if lStuff[0]==lStuff[1]:continue
    if iIdent>=95.0:
        
        #if lStuff[8]>iStart and lStuff[9]<iEnd:
            #continue            
        outputFile.write(sQuery)
        outputFile.write(lines)
        
    if iIdent>=60.0 and iIdent <95.0:
        
        outputFile2.write(sQuery)
        outputFile2.write(lines)
    if iIdent>=80.0 and iIdent <95.0:

        outputFile3.write(sQuery)
        outputFile3.write(lines)         
    

outputFile.close()
outputFile2.close()
outputFile3.close()
inputFile.close()
print "done"
