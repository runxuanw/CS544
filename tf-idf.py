from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

#Retrive processed data
file = open("wordprocessed.txt")
fileget = file.read().split("\n")
userInfo = eval(fileget[0])
queryList = eval(fileget[1])
file.close()

corpus = []

for item in queryList:
    for query in queryList[item]:
        if not query:
            break
        corpus.append(query)

vectorizer = CountVectorizer()
tf = vectorizer.fit_transform(corpus)

word = vectorizer.get_feature_names()

col,row=tf.T.nonzero()

index=[]
sum=0


tem=col[0]
print(len(col))
print(len(word))

output = open("feature.txt","w+")
output.write(str(word))