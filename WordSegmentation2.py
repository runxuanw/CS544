import jieba
import json

#Read stop word file
with open("zh.json") as stopwordfile:
    stopWord = json.load(stopwordfile)
    stopwordfile.close()

#Load word dictionary to improve word segmentation accuracy
jieba.load_userdict("sougou.dic")


file = open("dev_data.txt")
testfile = open("test_data_raw.txt")

outputfile = open("wordprocessed2.txt","w")
labelfile = open("wordlabel2.txt","w")
processedTestFile = open("testprocessed2.txt", "w")
#read file and segment word
for idx, line in enumerate(file):
    if idx > 10000:
        break
    if idx%100 == 0:
        print str(idx)
    
    line = line.strip()
    item = line.split("\t")    
    printLine = []
    '''print str(printLine)'''

    for i in range(4,len(item)):
        wordlist = jieba.cut_for_search(item[i])
        res = ""
        for word in wordlist:
            if word in stopWord:
                continue
            res += " " + word
        printLine.append(res)
    if idx > 0:
        labelfile.write(",")
        outputfile.write(",")
    
    labelfile.write(str(item[:4]))
    outputfile.write(str(printLine))

for idx, line in enumerate(testfile):
    if idx > 2000:
        break
    if idx%100 == 0:
        print str(idx)
    line = line.strip()
    item = line.split("\t")   
    printLine = []
    for i in range(1,len(item)):
        wordlist = jieba.cut_for_search(item[i])
        res = ""
        for word in wordlist:
            if word in stopWord:
                continue
            res += " " + word
        printLine.append(res)
    if idx > 0:
        processedTestFile.write(",")
    processedTestFile.write(str(printLine))

processedTestFile.close()
outputfile.close()
labelfile.close()
print "done"