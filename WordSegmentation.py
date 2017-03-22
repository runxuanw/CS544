import jieba
file = open("dev_data.txt")
#File's total line number is 20000, set 75% (15000 lines) as development data
userInfo = {}
queryList = {}
for line in file:
    line = line.strip()
    item = line.split("\t")
    usrID = item[0]
    userInfo[usrID] = {}
    userInfo["age"] = item[1]
    userInfo["gen"] = item[2]
    userInfo["edu"] = item[3]
    for i in range(4,len(item)):
        if (i == 4):
            queryList[usrID] = []
        query = item[i]
        wordlist = jieba.cut_for_search(query)
        res = ",".join(wordlist)
        #print res
        queryList[usrID].append(res)