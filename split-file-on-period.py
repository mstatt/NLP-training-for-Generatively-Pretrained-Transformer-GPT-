#script to format soap-text.txt file for more sensible training
import string, re

# Set desired length of sentences 
sentLength = 50

with open("soap-text.txt", "r") as fic:
    content = fic.read()

sentences = content.split(".")
sentences = [s.strip() for s in sentences]

file2 = open("training-text-formatted.txt",'w')
for line in sentences:
    line = line.replace("  ", " ")
    line = line.replace("@", "")
    line = line.replace("!", "")
    line = line.replace("?", "")
    line = line.replace("-", "")
    line = line.replace("  ", " ")
    line = line.replace("?", "")
    line = line.replace("#", "")
    line = line.replace("#", "")
    line = line.replace(" , ", ", ")
    line = line.replace(" '", "'")
    line = line.replace(" n't", "n't")
    line = line.replace("  ", " ")
    line = re.sub("[\(\[].*?[\)\]]", "", line)
    
    if(len(line) >= sentLength):
        try:
            intIndex = line.index(" ")
            strIntr = line[:intIndex]
            int(strIntr)
            flag = True
        except ValueError:
                flag = False

        if (flag):
            strLine = line[intIndex:]
        else:
            strLine = line

        try:
            intIndex2 = strLine.index(":")
            strIntr2 = strLine[:intIndex2 +1]
            strLine = strLine.replace(strIntr2, "")
            flag2 = True
        except ValueError:
                flag2 = False


        if(len(strLine) >= sentLength):
            file2.write(strLine.strip()+".\n")
