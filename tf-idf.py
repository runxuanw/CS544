from __future__ import division
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn import svm, model_selection
import math
from sklearn.feature_selection import chi2
import time
import numpy as np
from sklearn.feature_selection import SelectKBest,chi2


#Retrive processed data
file = open("wordprocessed.txt")
fileget = file.read().split("\n")
userInfo = eval(fileget[0])
queryList = eval(fileget[1])
file.close()

corpus = []

for item in queryList:
    temp = ""
    for query in queryList[item]:
        if not query:
            break
        temp = temp + query + "\t"
    corpus.append(temp)

vectorizer = CountVectorizer()
tf = vectorizer.fit_transform(corpus)

word = vectorizer.get_feature_names()

def test(train,label):

    label2=[]
    index=[]
    for i in range(len(label)):
        if(label[i]!=0):
            label2.append(label[i])
            index.append(i)
    print((len(label2)))



    train=train[index,:]



    X_train, X_test, y_train, y_test = model_selection.train_test_split(train, label2, test_size = 0.2, random_state = 0)

    """
    sk=SelectKBest(chi2,k=100000)

    sk.fit(X_train, y_train)

    X_train=sk.transform(X_train)
    X_test=sk.transform(X_test)

    """

    #clf=RandomForestClassifier(n_estimators=20).fit(X_train, y_train)
    #clf = xgb.fit(X_train, y_train)



    clf = svm.LinearSVC(C=0.24).fit(X_train, y_train)

    #clf = svm.SVC(kernel='rbf',degree=7,gamma=0.000001).fit(X_train, y_train)
    res=clf.score(X_test,y_test)

    #res = clf.predict(X_test)


    """
    param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'binary:logistic'}
    bst = xgb.train(param, X_train, 2)
    preds = bst.predict(X_test)

    count=0;
    for i in range(len(y_test)):
        if preds[i]==y_test[i] :
            count=count+1
    res=count/len(y_test)
    """

    return res

row,col=tf.T.nonzero()

tf=np.ceil(tf/5)
#tf=np.log1p(tf)



transformer = TfidfTransformer()
tfidf = transformer.fit_transform(tf)

print(tfidf.nnz)


label1 = []
label2 = []
label3 = []
for user in userInfo:
    label1.append(userInfo[user]["age"])
    label2.append(userInfo[user]["gen"])
    label3.append(userInfo[user]["edu"])

label1 = [ int(label1) for label1 in label1 if label1 ]
label2 = [ int(label2) for label2 in label2 if label2 ]
label3 = [ int(label3) for label3 in label3 if label3 ]

train = []
for i in range(15000):
    train.append(i)

train_x = tfidf[train,:]

res1=test(train_x,label1)
res2=test(train_x,label2)
res3=test(train_x,label3)

print(res1)
print(res2)
print(res3)

print((res1+res2+res3)/3)