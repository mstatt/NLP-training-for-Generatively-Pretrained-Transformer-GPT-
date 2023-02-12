#script to format soap-text.txt file for more sensible training
"""
10 Feb Michael J. Stattelman
If this script is ran in the current configuration, 
it will generate a file of 9 million words with a character count of over 55 million.
"""
import string, re, os

# Set desired length of sentences 
sentLength = 30

soapFile = "data/soap-text.txt"
newsFile = "data/news-text.txt"
tvmFile = "data/tvm-text.txt"
blogFile = "data/blog-text.txt"
acadFile = "data/acad-text.txt"
magFile = "data/mag-text.txt"
ficFile = "data/fic-text.txt"
spokFile = "data/spok-text.txt"


def cleanText(cleanFile, txtname):
    """
    Function to clean and format downloaded text file.
    """
    with open(cleanFile, "r") as fic:
        content = fic.read()
        sentences = content.split(".")
        sentences = [s.strip() for s in sentences]

        file2 = open(txtname+"-training-text-formatted.txt",'w')
        for line in sentences:
            line = line.lstrip()
            line = line.replace("  ", " ")
            line = line.replace('""', '')
            line = line.replace("@", "")
            line = line.replace("<p>", "")
            line = line.replace("</p>", "")
            line = line.replace("<h>", "")
            line = line.replace("</h>", "")
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

    return txtname+"-training-text-formatted.txt"        


def mergeTrainingFiles(tfile1,tfile2,nameEnd):
    """
    Function to merge both training file into a large one.
    """
    data = data2 = ""
    # Reading data from file1
    with open(tfile1) as fp:
        data = fp.read()
      
    # Reading data from file2
    with open(tfile2) as fp:
        data2 = fp.read()
      
    # Merging 2 files
    # To add the data of file2
    # from next line
    data += "\n"
    data += data2
      
    with open (nameEnd+'-training-text-formatted.txt', 'w') as fp:
        fp.write(data)

    return nameEnd+'-training-text-formatted.txt'

file1 = cleanText(soapFile, "soap")
file2 = cleanText(newsFile, "news")
file3 = cleanText(tvmFile, "tvm")
file4 = cleanText(blogFile, "blog")
file5 = cleanText(acadFile, "acad")
file6 = cleanText(magFile, "mag")
file7 = cleanText(ficFile, "fic")
file8 = cleanText(spokFile, "spok")




partA = mergeTrainingFiles(file1,file2,'partA')
partB = mergeTrainingFiles(file3,file4,'partB')
# Secondary merge
partC = mergeTrainingFiles(file5,file6,'partC')
partD = mergeTrainingFiles(file7,file8,'partD')
# Tirteary merge
partialA = mergeTrainingFiles(partA,partB,'merged-partialA')
partialB = mergeTrainingFiles(partC,partD,'merged-partialB')
#Final merge with sentence length prepended to the name
final = mergeTrainingFiles(partialA,partialB,str(sentLength)+'-merged-final')

# Delete all unmecessary files to avoid conflicts.

os.remove(file1)
os.remove(file2)
os.remove(file3)
os.remove(file4)
os.remove(file5)
os.remove(file6)
os.remove(file7)
os.remove(file8)
os.remove(partA)
os.remove(partB)
os.remove(partC)
os.remove(partD)
os.remove(partialA)
os.remove(partialB)
# One final pass for clean up.
cleanText(final, str(sentLength)+'-final')
# Delete the last file
os.remove(final)