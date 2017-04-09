from __future__ import division
'''
the line in input file should be seperated by tab:
22DD920316420BE2DF8D6EE651BA174B    1    1    4

how to use:
acc = getAccuracy("predict.txt", "test_data_tagged.txt")
print "precision: "+str(acc[0])+"\n"
print "recall: "+str(acc[1])+"\n"
'''

'''
def getAccuracy(predictFile, labelFile):
    cntpredictLine = 0
    cntlabelLine = 0
    matchedLabel = 0
    lineIdx = -1
    file = open(predictFile, "r")
    predicts = []
    for line in file:
        line = line.strip("\n").split("\t")
        predicts.append(line)
        cntpredictLine += 1
    file.close()
    
    file = open(labelFile, "r")
    for line in file:
        lineIdx = lineIdx + 1
        cntlabelLine += 1
        line = line.strip("\n").split("\t")
        if cntlabelLine <= cntpredictLine:
            for i in range(4):
                if i != 0:
                    if predicts[lineIdx][i] == line[i]:
                        matchedLabel += 1
    
    return matchedLabel*1.0/(cntpredictLine*3.0), matchedLabel*1.0/(cntlabelLine*3.0)
            
acc = getAccuracy("predict.txt", "test_data_tagged.txt")
print "precision: "+str(acc[0])+"\n"
print "recall: "+str(acc[1])+"\n"
'''
file = open("predict.txt", "r")
label1_pre = []
label2_pre = []
label3_pre = []

for line in file:
    item = line.strip("\n").split("\t")
    label1_pre.append(item[1])
    label2_pre.append(item[2])
    label3_pre.append(item[3])
file.close()

label1_ref = []
label2_ref = []
label3_ref = []
fileTagged = open("test_data_tagged.txt","r")
for line in fileTagged:
    line = line.strip()
    item = line.split("\t")
    label1_ref.append(item[1])
    label2_ref.append(item[2])
    label3_ref.append(item[3])
fileTagged.close()


res1 = res2 = res3 = 0
for i in range(5000):
    if (label1_pre[i] == label1_ref[i]):
        res1 = res1 + 1
    if (label2_pre[i] == label2_ref[i]):
        res2 = res2 + 1
    if (label3_pre[i] == label3_ref[i]):
        res3 = res3 + 1

print res1/5000
print res2/5000
print res3/5000
print (res1+res2+res3)/15000