#CONVERSOR METHYLKIT OUTPUT TO BEDGRAPH
#ALEJANDRA RODRIGUEZ SOSA

#!/usr/bin/env python3

from sys import argv 
import re
import os
import glob
import time

#Check script execution time
start = time.time()

#Prompts user for input file - TESTING PURPOSES ONLY
#files = input("Introduce file name: ")
#Prompts user for path and change to that path 
#path = input("Introduce full path: ")
#os.chdir(path)

#Get list of file names from directory in a 
list_files = glob.iglob('/home/alejandrarodrigu21/Documents/ROGERS_SAMPLES/*.methylKit', recursive = False)

#Pattern dictionaries:
#Match all characters at the beginning of the line until first tab  
#Match letter + tab combination - for R/F strand 
#Mitochondrial and sex chromosomes - match ONLY R/F until tab
replacements = [(r"^[^\t]*", ""),(r"[A-Z]\t", "")]
MTXY_replacements = [(r"^[^\t]*", ""),(r"[RF]\t","")]

#Open file and iterate over lines to remove first line
#Read and write different files instead of overwriting - prevents losing data

for file in list_files:
	#print(file)	
	with open(file, "r") as f, open (os.path.join('/home/alejandrarodrigu21/Documents/ROGERS_SAMPLES/', os.path.basename(file))+"_converted", "w") as fo:
		for line in f:
			MT = re.findall("^MT", line)
			Y = re.findall("^Y", line)
			X = re.findall("^X", line)
			if not Y and not X and not MT:
				#Iterate over list to perform regex substitutions
				for old, new in MTXY_replacements:
					line = re.sub(old, new, line)
				#Remove trailing space at start of line
				line = line.strip()
				fo.writelines(line+"\n")
			else:
				for old, new in MTXY_replacements:
					line = re.sub(old, new, line)
				line = line.strip()
				fo.writelines(line+"\n")
		

end = time.time()
print(end - start)
