from sklearn import svm

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
import numpy as np
import jieba
import json

#Read stop word file
with open("zh.json") as stopwordfile:
    stopWord = json.load(stopwordfile)
    stopwordfile.close()

jieba.load_userdict("sougou.dic")


#Retrive processed data
file = open("wordprocessed.txt")
fileget = file.read().split("\n")
userInfo = eval(fileget[0])
queryList = eval(fileget[1])
file.close()

corpus = []
userID = []
for item in queryList:
    temp = ""
    for query in queryList[item]:
        if not query:
            break
        temp = temp + query + "\t"
    corpus.append(temp)

fileRaw = open("test_data_raw.txt")
for line in fileRaw:
    line = line.strip()
    item = line.split("\t")
    userID.append(item[0])
    tempstr = ""
    for i in range(1,len(item)):
        query = item[i]
        wordlist = jieba.cut_for_search(query)
        res = ""
        for word in wordlist:
            if word in stopWord:
                continue
            res += " " + word
        tempstr = tempstr + res + "\t"
    corpus.append(tempstr)

vectorizer = CountVectorizer()

#Fit the model according to the given training data.
#Fit to data, then transform it.
tf = vectorizer.fit_transform(corpus)
tf=np.ceil(tf/100)

word = vectorizer.get_feature_names()
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(tf)

label1 = []
label2 = []
label3 = []
for user in userInfo:
    label1.append(userInfo[user]["age"])
    label2.append(userInfo[user]["gen"])
    label3.append(userInfo[user]["edu"])

label1 = [int(label1) for label1 in label1 if label1]
label2 = [int(label2) for label2 in label2 if label2]
label3 = [int(label3) for label3 in label3 if label3]

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

    clf = svm.LinearSVC(C=0.24).fit(train_x, label)

    #Predict class labels for samples in test_x
    res = clf.predict(test_x)
    print(res)
    return res

label1_pre=predict(train_x,label1,test_x)
label2_pre=predict(train_x,label2,test_x)
label3_pre=predict(train_x,label3,test_x)

output = open("predict.txt","w")
for i in range(5000):
    output.write(str(userID[i])+"\t"+str(label1_pre[i])+"\t"+str(label2_pre[i])+"\t"+str(label3_pre[i])+"\n")
output.close()
