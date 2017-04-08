'''
the line in input file should be seperated by tab:
22DD920316420BE2DF8D6EE651BA174B    1    1    4

how to use:
acc = getAccuracy("predict.txt", "test_data_tagged.txt")
print "precision: "+str(acc[0])+"\n"
print "recall: "+str(acc[1])+"\n"
'''


def getAccuracy(predictFile, labelFile):
    cntpredictLine = 0
    cntlabelLine = 0
    matchedLabel = 0
    file = open(predictFile, "r")
    predicts = []
    for line in file:
        line = line.strip("\n").split("\t")
        predicts.append(line)
        cntpredictLine += 1
    file.close()
    
    file = open(labelFile, "r")
    for lineIdx, line in enumerate(file):
        cntlabelLine += 1
        line = line.strip("\n").split("\t")
        if cntlabelLine <= cntpredictLine:
            for i in range(4):
                if i != 0:
                    if predicts[lineIdx][i] == line[i]:
                        matchedLabel += 1
    
    return matchedLabel*1.0/(cntpredictLine*3.0), matchedLabel*1.0/(cntlabelLine*3.0)
            
