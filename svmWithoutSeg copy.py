import json

from sklearn import svm
from re import compile as _Re

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

with open("zh.json") as stopwordfile:
    stopWord = json.load(stopwordfile)
    stopwordfile.close()

file = open("dev_data.txt")
corpus = []
label1 = []
label2 = []
label3 = []
userID = []
for line in file:
    line = line.strip()
    item = line.split("\t")
    label1.append(item[1])
    label2.append(item[2])
    label3.append(item[3])

    tempCor = ""
    for i in range(4,len(item)):
        tempChar = list(item[i].decode('utf-8'))
        tempStr = ""
        for temp in tempChar:
            if temp != "":
                if temp in stopWord:
                    continue
                tempStr = tempStr + " " + temp
        tempCor += tempStr + "\t"
    corpus.append(tempCor)

fileRaw = open("test_data_raw.txt")
for line in fileRaw:
    line = line.strip()
    item = line.split("\t")
    userID.append(item[0])
    tempCor = ""
    for i in range(1,len(item)):
        tempChar = list(item[i].decode('utf-8'))
        tempStr = ""
        for temp in tempChar:
            if temp != "":
                if temp in stopWord:
                    continue
                tempStr = tempStr + " " + temp
        tempCor += tempStr + "\t"
    corpus.append(tempCor)

vectorizer = CountVectorizer()

#Fit the model according to the given training data.
#Fit to data, then transform it.
tf = vectorizer.fit_transform(corpus)
tf=np.ceil(tf/100)

word = vectorizer.get_feature_names()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(tf)

train = []
test = []

for i in range(20000):
    if (i< 15000):
        train.append(i)
    else:
        test.append(i)

#extract index train
train_x=tfidf[train,:]

test_x=tfidf[test,:]


def predict(train_x,train_y,test_x):

    label=[]
    index=[]
    for i in range(len(train_y)):
        if(train_y[i]!=0):
            label.append(train_y[i])
            index.append(i)
    print((len(label2)))
    train_x=train_x[index,:]

    clf = svm.LinearSVC(C=0.28).fit(train_x, label)

    #Predict class labels for samples in test_x
    res = clf.predict(test_x)
    print(res)
    return res

label1_pre=predict(train_x,label1,test_x)
label2_pre=predict(train_x,label2,test_x)
label3_pre=predict(train_x,label3,test_x)

output = open("svmWithoutSeg.txt","w")
for i in range(5000):
    output.write(str(userID[i])+"\t"+str(label1_pre[i])+"\t"+str(label2_pre[i])+"\t"+str(label3_pre[i])+"\n")
output.close()
