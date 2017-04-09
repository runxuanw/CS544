import jieba
import json

#Read stop word file
with open("zh.json") as stopwordfile:
    stopWord = json.load(stopwordfile)
    stopwordfile.close()

#Load word dictionary to improve word segmentation accuracy
jieba.load_userdict("sougou.dic")

#File's total line number is 20000, set 75% (15000 lines) as development data
file = open("dev_data.txt")
#user's information matrix
userInfo = {}
#user's query list
queryList = {}

#read file and segment word
for line in file:
    line = line.strip()
    item = line.split("\t")
    usrID = item[0]
    userInfo[usrID] = {}
    if (float(item[1]).is_integer()):
        userInfo[usrID]["age"] = item[1]
    else:
        print "check"
    if (float(item[2]).is_integer()):
        userInfo[usrID]["gen"] = item[2]
    else:
        print "check2"
    if (float(item[3]).is_integer()):
        userInfo[usrID]["edu"] = item[3]
    else:
        print "check3"
    for i in range(4,len(item)):
        if (i == 4):
            queryList[usrID] = []
        query = item[i]
        wordlist = jieba.cut_for_search(query)
        res = ""
        for word in wordlist:
            if word in stopWord:
                continue
            res += " " + word
        queryList[usrID].append(res)

outputfile = open("wordprocessed.txt","w")
outputfile.write(str(userInfo)+"\n")
outputfile.write(str(queryList)+"\n")