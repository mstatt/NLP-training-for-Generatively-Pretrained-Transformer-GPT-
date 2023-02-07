#Clean and format the Big Bang Theory Script for model training.
"""
Scripts scraped from https://bigbangtrans.wordpress.com/
"""

import re

startFile = 'BBT-S1-S10.txt'
updatedFile = 'BBT-S1-S10-Updated.txt'
finalFile = 'BBT-S1-S10-Final.txt'

file1 = open(startFile,'r')

# defining object For intermediary to open file in write mode
file2 = open(updatedFile,'w')

# reading each line from original text file
for line in file1.readlines():
	# reading all lines that do not begin with Whatever word
	if not (line.startswith('Scene')):
		# printing those lines
		# print(line)
		# writing only those lines that do not begin with Whatever word
		file2.write(line)

# close and save the files
file2.close()
file1.close()

#Remove empty lines and content inside of ()'s'
with open(updatedFile,"r") as f, open(finalFile,"w") as outfile:
 for i in f.readlines():
		if not i.strip():
			continue

		if i:
				h = re.sub("[\(\[].*?[\)\]]", "", i)
				outfile.write(h)
 			

