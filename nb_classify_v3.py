# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 23:02:49 2017

@author: chenliangxs
"""

import math

modelFile=open("nbmodel.txt")
nbData=modelFile.read().split("\n")
agePrior=eval(nbData[0])
genPrior=eval(nbData[1])
eduPrior=eval(nbData[2])
ageDictionary=eval(nbData[3])
genDictionary=eval(nbData[4])
eduDictionary=eval(nbData[5])
modelFile.close()
#output=open("testoutput.txt","w")
#output.write(str(ageDictionary))
#output.close()
#print("read")
verifyFile=open("wordprocessed_forVerify.txt")
verifyData=eval(verifyFile.read())
print("start")

#user info id->age, gender, education
userInfo={}

#user queries for test. id->queries
userQuery={}

for lineKey in verifyData.keys():
    userID=lineKey
    queries=verifyData[lineKey]
    ageProb=list(agePrior)
    genProb=list(genPrior)
    eduProb=list(eduPrior)
    for query in queries:
        words=query.split()
        for word in words:
            if word in ageDictionary.keys():
                for i in range(7):
                    if agePrior[i]>0:
                        ageProb[i]+=ageDictionary[word][i]
                for i in range(3):
                    if genPrior[i]>0:
                        genProb[i]+=genDictionary[word][i]
                for i in range(7):
                    if eduPrior[i]>0:
                        eduProb[i]+=eduDictionary[word][i]
    maxAge=0
    maxGen=0
    maxEdu=0
    maxAgeProb=float('-inf')
    for i in range(7):
        if ageProb[i]!=0:
            maxAgeProb=max(maxAgeProb, ageProb[i])
            if maxAgeProb==ageProb[i]:
                maxAge=i
    maxGenProb=float('-inf')
    for i in range(3):
        if genProb[i]!=0:
            maxGenProb=max(maxGenProb, genProb[i])
            if maxGenProb==genProb[i]:
                maxGen=i                            
    maxEduProb=float('-inf')
    for i in range(7):
        if eduProb[i]!=0:
            maxEduProb=max(maxEduProb, eduProb[i])
            if maxEduProb==eduProb[i]:
                maxEdu=i
    tags=maxAge+" "+maxGen+" "+maxEdu
    userInfo[userID]=tags                         
    '''
    for i in range(7):
        maxProb=float('-inf')
        if agePrior[i]>0:
            ageProb[i]+=math.log10(agePrior[i])
            for query in queries:
                words=query.split(" ")
                for word in words:
                    if word in ageDictionary.keys():
                        #print str(word)
                        ageProb[i]+=ageDictionary[word][i]
            maxProb=max(maxProb, ageProb[i])
            if maxProb==ageProb[i]:
                maxAge=i
    for i in range(3):
        maxProb=float('-inf')
        if genPrior[i]>0:
            genProb[i]+=math.log10(genPrior[i])
            for query in queries:
                words=query.split()
                for word in words:
                    if word in genDictionary.keys():
                        genProb[i]+=genDictionary[word][i]
            maxProb=max(maxProb, genProb[i])
            if maxProb==genProb[i]:
                maxGen=i
    for i in range(7):
        maxProb=float('-inf')
        if eduPrior[i]>0:
            eduProb[i]+=math.log10(eduPrior[i])
            for query in queries:
                words=query.split(" ")
                for word in words:
                    if word in eduDictionary.keys():
                        eduProb[i]+=eduDictionary[word][i]
            maxProb=max(maxProb, eduProb[i])
            if maxProb==eduProb[i]:
                maxGen=i
    userInfo[userID]=[maxAge, maxGen, maxEdu]
    '''

verifyFile.close()

#output with tags: age, gender, education
output=open("resultAfterTagging.txt", "w")
output.write(str(userInfo))
output.close()
    
        
    
    
    
    
