#!/usr/bin/python
#Program for creating graphs for GC


import os, sys ,fnmatch , numpy, collections,xlsxwriter

sys.argv
def findFiles (path, filter):
    for root, dirs, files in os.walk(path):
        for file in fnmatch.filter(files, filter):
            yield os.path.join(root, file)




newfile= sys.argv[1]
date = sys.argv[2]
standards = int(sys.argv[3])
vheadspace = float(sys.argv[4])
workoook = newfile.split(".")[0] + "GC_info"+".csv"
#output =open(workook, "w")
#workbook = xlsxwriter.Workbook(workook)
#worksheet = workbook.add_worksheet()
#outputfile = open("/Users/NikolasStrepis/Documents/GC_graphs.xls", "W")


newfila =open(newfile)
output = open (workoook, "w")

header = date + "\t" + newfila.readline()
#worksheet.write(header)

type(newfila)

mol02stand = float(0.0002/(0.082*(20+273)))

num_lines = sum(1 for line in open(newfile))
dict2={}
dict3={}
linesb=""
value=1
dict1={}
dict4={}
#chart = workbook.add_chart({'type': 'column'})
areab=[]
numberab =[]
if standards  == 1 or standards ==2 or standards ==3 :

	for index, lines in enumerate(newfila) and not str(lines.strip().split(";")[2]) != "Area":
		print str(lines.strip().split(";")[2])
		if "Mark" in lines:
			print lines
			pass
 	# 	if float(lines.strip().split(";")[0].replace(",",".")) >10000 :
			
		# 	comp = lines.strip().split(";")[8]
		# 	value = float(lines.strip().split(";")[2].replace(",",".")) 
		# 	number= lines.strip().split(";")[0]
		# 	#print value
			 
		# 	#print value
		# 	if linesb !="":
		# 		value1 = float(linesb.strip().split(";")[2].replace(",",".")) 
			
		# 		valuefinal = (value + value1)/2
				
		# 		dict2[comp]=valuefinal
		# 		#print valuefinal
		# 	linesb=lines
		# else:
		
		# 	area = lines.strip().split(";")[2].replace(",",".")
		# 	#print area
		# 	compound = lines.strip().split(";")[8]
		# 	numbera= lines.strip().split(";")[0]
		# 	numberab = [numbera] + numberab
		# 	areab = [area] + areab
		# 	dict1[compound] = numbera, areab
		# 	#print numberab
		# #	dict4[numbera] = areab

data=""
sumaras =0
for key in dict1:
	numberb, areabs = dict1[key]
	
	for i in areab:
		sumaras = sumaras + 1

		data = float(((float(i)*mol02stand/float(dict2[key])*1000)*vheadspace/0.2)/vheadspace*1000)
		stage = numberab[sumaras-1]

		
		print key + "\t" +"\t" + stage + "\t" +str(data) 
		#worksheet.write_column(key, data)	
		output.write(key + "\t"  + stage + "\t" +str(data) +"\n" )
		





# dict1={}

# chart = workbook.add_chart({'type': 'column'})

# for index,lines in enumerate(newfila):
# 	print lines
# 	area = lines.strip().split(";")[2]

# 	compound = lines.strip().split(";")[8]

# 	dict1[compound] = area

# data=""
# for key in dict1:
# 	data = int(((dict1[key]*mol02stand/dict2[key]*1000)*vheadspace/0.2)/vheadspace*1000)
# 	print data
# 	worksheet.write_column(key, data)


#workbook.close()
