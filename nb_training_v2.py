import math
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer, TfidfVectorizer

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

vectorizer2 = TfidfVectorizer()
tfidf = vectorizer2.fit_transform(corpus)
wordFeature = vectorizer2.get_feature_names()

dense = tfidf.todense()
episode = dense[0].tolist()[0]
phrase_scores = [pair for pair in zip(range(0, len(episode)), episode) if pair[1] > 0]
print len(phrase_scores)
wordFeature2 = []
for number in phrase_scores:
    wordFeature2.append(wordFeature[number[0]])


print wordFeature2

# word dictionary for age(0-10). word->
age_dictionary = {}
gender_dictionary = {}
education_dictionary = {}

# count total in users
ageCount = [0] * 7
genderCount = [0] * 3
educationCount = [0] * 7
totalUser = 0

# count total for words
ageForWords = [0] * 7
genderForWords = [0] * 3
educationForWords = [0] * 7

for id in queryList:
    queries = queryList[id]
    age = (int)(userInfo[id]["age"])
    gender = (int)(userInfo[id]["gen"])
    education = (int)(userInfo[id]["edu"])
    totalUser += 1
    ageCount[age] += 1
    genderCount[gender] += 1
    educationCount[education] += 1
    for query in queries:
        words = query.split()
        for word in words:
            if word in wordFeature2:
                if word in age_dictionary.keys():
                    age_dictionary[word][age] += 1
                    ageForWords[age] += 1
                    # print (str(age_dictionary[word][age]))
                    gender_dictionary[word][gender] += 1
                    genderForWords[gender] += 1
                    education_dictionary[word][education] += 1
                    educationForWords[education] += 1
                else:
                    age_dictionary[word] = [0] * 7
                    age_dictionary[word][age] = 1
                    ageForWords[age] += 1
                    # print(str(age_dictionary[word][age]))
                    gender_dictionary[word] = [0] * 3
                    gender_dictionary[word][gender] = 1
                    genderForWords[gender] += 1
                    education_dictionary[word] = [0] * 7
                    education_dictionary[word][education] = 1
                    educationForWords[education] += 1
print len(age_dictionary)
#prior probabilities
age_priorP=[0]*7
gender_priorP=[0]*3
education_priorP=[0]*7
for i in range(7):
    age_priorP[i]=(1.0*ageCount[i]/totalUser)
for i in range(3):
    gender_priorP[i]=(1.0*genderCount[i]/totalUser)
for i in range(7):
    education_priorP[i]=(1.0*educationCount[i]/totalUser)

#smoothing and calculate P(word/age)
B_factor=len(age_dictionary)
for word in age_dictionary:
    for i in range(7):
        age_dictionary[word][i]=math.log10(1.0*(age_dictionary[word][i]+1)/(ageForWords[i]+B_factor))
for word in gender_dictionary:
    for i in range(3):
        gender_dictionary[word][i]=math.log10(1.0*(gender_dictionary[word][i]+1)/(genderForWords[i]+B_factor))
for word in education_dictionary:
    for i in range(7):
        education_dictionary[word][i]=math.log10(1.0*(education_dictionary[word][i]+1)/(educationForWords[i]+B_factor))

output=open("nbmodel.txt","w")
output.write(str(age_priorP)+'\n')
output.write(str(gender_priorP)+'\n')
output.write(str(education_priorP)+'\n')
output.write(str(age_dictionary)+'\n')
output.write(str(gender_dictionary)+'\n')
output.write(str(education_dictionary)+'\n')
output.close()


