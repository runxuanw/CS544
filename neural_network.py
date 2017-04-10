from sklearn import svm
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy as np
from getAccuracy2 import getAccuracy2

def appendCorpus(corpus, segArray):
    cnt = 0
    for idx, entry in enumerate(segArray):
        line = ""
        cnt = idx+1
        for seg in entry:
            line += seg + "\t"
        corpus.append(line)
    return cnt

def trainAndPredict(trainx, trainy, testx):
    print "one predict section start"
    clf = svm.LinearSVC(C=0.24).fit(trainx, trainy)
    clf = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1).fit(trainx, trainy)

    res = clf.predict(testx)
    print "one predict section done"
    return res
    

labelfile = open("wordlabel2.txt", 'r')
wordfile = open("wordprocessed2.txt", 'r')
rawfile = open("testprocessed2.txt", 'r')

segments = eval(wordfile.read())
labels = eval(labelfile.read())
testSeg = eval(rawfile.read().split('\n'))

labelAge = []
labelEdu = []
labelGen = []
corpus = []
predictRes = []
testCnt = 0
trainCnt = 0

for item in labels:
    labelAge.append(int(item[1]))
    labelGen.append(int(item[2]))
    labelEdu.append(int(item[3]))

testCnt = appendCorpus(corpus, testSeg)
trainCnt = appendCorpus(corpus, segments)


vectorizer = CountVectorizer()
tf = vectorizer.fit_transform(corpus)
tf = np.ceil(tf/100)

word = vectorizer.get_feature_names()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(tf)

train = []
test = []
for i in range(testCnt+trainCnt):
    if (i < trainCnt):
        train.append(i)
    else:
        test.append(i)
        
train_x=tfidf[train,:]
test_x=tfidf[test,:]


predictRes.append(trainAndPredict(train_x, labelAge, test_x))
predictRes.append(trainAndPredict(train_x, labelGen, test_x))
predictRes.append(trainAndPredict(train_x, labelEdu, test_x))

output = open("predictNN.txt","w")
for i in range(testCnt):
    output.write(str("id")+"\t"+str(predictRes[0][i])+"\t"+str(predictRes[1][i])+"\t"+str(predictRes[2][i])+"\n")
output.close()

getAccuracy2("predictNN.txt", "test_data_tagged.txt")

print "done"