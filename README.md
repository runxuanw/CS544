# CS544 NLP project
## Introduction of project
In this project, we have a set of users' information and users' search history from a Chinese search engine, we will develop a system to predict users' information, based on their search history.

The following is an example of data set.

E36710951AD5D8379F85FFBFCF46780E	1	1	5	藏御堂28泡	大丈夫功名未成	小米概念机	藏秘28泡	贾汪	功夫少林纪录片	华为商城	秦时明月之君临天下	l是多大号的衣服	小米note2概念机	健胃消食片	张书省	海鲜菇的做法	搞笑动态图片	秦时明月之诸子百家全集	优酷下载	苹果4s	扣扣下载	好男儿志在四方	重做手机系统	如何才能成就一番事业	为什么秋冬进补	cf陈子豪	藏御堂28泡怎么样	oppo a617	丛大夫	补气血的中药	移动网上营业厅	红米手机重做系统	木头城子到朝阳客车	血未冷	健脾丸康爱多	如何成就一番事业	28泡脚	章子怡发誓再也不拍功夫片	龙泉宝剑	血未冷,梦还滚烫	换个喇叭多少钱	小米2es	古代形容当兵的诗句	健脾丸的功效与作用	高山流水古筝曲	杨角沟到喀左	大枣吃多了会上火吗	苹果5s怎么样	红米note重做系统	cf官网	乱斗西游那个英雄厉害	华为5a	360手机	照身份证多长时间能下来	腾讯手机管家	红米1s	m4黑龙	大丈夫事业未成,何以为家	无极剑圣	无锋剑	vivo	功夫少林	vivo官网	党参的功效与作用	手机换个喇叭多少钱	关于当兵的诗句	吃大枣上火怎么办	东皇太一	龙眼肉的功效与作用	好男儿就是要当兵	苹果5s	oppoa31	移动卡号码选号	中关村在线	oppoa33	黑龙	搜狗地图	藏御堂28泡是假的吗	换个充电接口多少钱	oppoa37	唐刀	治疗神经衰弱的中草药	成就事业的句子	m4a1	移动卡号码选号辽宁	功夫少林纪录片的背景音乐	oppoa59	旷修	大枣的功效与作用	办理移动卡	龙眼肉	oppo a90	藏秘二十八泡状况反应	cf刷枪有谁成功	喀左有网吧吗	治疗神经衰弱的中药	藏密28泡	跑酷视频	朝阳县丛大夫	秋冬进补的道理	m4a1黑龙	如何才能成就大事	治疗神经衰弱的药物	l是多大号的衣服男	快照身份证需要多长时间	华为4a

The first hash string is that user's ID.

The first integer label is user's age label, there are 7 possible values for age label, each value and its meaning is listed below.

| Age label value | Meaning          |
| ----------------| -----------------|
| 0               | unknown          |
| 1               | 0-18 years old   |
| 2               | 19-23 years old  |
| 3               | 24-30 years old  |
| 4               | 31-40 years old  |
| 5               | 41-50 years old  |
| 6               | 51-999 years old |

The second integer label is user's gender label, there are 3 possible values for gender label, each value and its meaning is listed below.

| Gender label value| Meaning |
| ------------------| --------|
| 0                 | unknown |
| 1                 | male    |
| 2                 | female  |

The third integer label is user's education label, there are 7 possible values for education label, each value and its meaning is listed below.

| Education label value| Meaning       |
| ---------------------| --------------|
| 0                    | unknown       |
| 1                    | PhD           |
| 2                    | Master        |
| 3                    | Bachelor      |
| 4                    | High School   |
| 5                    | Middle School |
| 6                    | Primary School|

The rest of the data example is user's seach hisory. Each query is seperated by "\t".

I seperated the data into training and testing parts, traning is 75% of total (15000 lines), and testing is 25% (5000 lines).

## Tools we use
https://github.com/fxsjy/jieba This is the word segmentation tool I used.

Output file of WordSegmentation.py is wordprocessed.txt. Output file has two lines, the first line is user ID and user information, second line is user ID and user query. You can use code snippet like following to retrive data and store them as a two dimensional array.
```Python
file = open("wordprocessed.txt")
fileget = file.read().split("\n")
userInfo = eval(fileget[0])
queryList = eval(fileget[1])
```

zh.json is stop word list, sougou.dic is a Chinese word tag dictionary, both are used to improve word segmentation accuracy.

sklearn is the library we use for td-idf feature selection + SVM classification. http://scikit-learn.org/stable/modules/svm.html#svm

##Results we get
--SVM Wtih Word Segmentation Accuracy-----------_
age: 0.5714_
gender: 0.8062_
education: 0.55_
average: 0.642533333333_
--Naive Bayes With Word Segmentation Accuracy---_
age: 0.2474_
gender: 0.485_
education: 0.2328_
average: 0.321733333333_
--SVM Wtihout Word Segmentation Accuracy--------_
age: 0.438_
gender: 0.6932_
education: 0.4324_
average: 0.5212_
--Neural Network Accuracy-----------------------_
age: 0.4756_
gender: 0.785_
education: 0.4176_
average: 0.5594_
