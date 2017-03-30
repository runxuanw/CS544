# CS544 NLP project
I seperated the data into training and testing parts, traning is 75% of total (15000 lines), and testing is 25% (5000 lines).
https://github.com/fxsjy/jieba This is the word segmentation tool I used.
<<<<<<< HEAD
<<<<<<< HEAD
Output file of WordSegmentation.py is wordprocessed.txt. Output file has two lines, the first line is user ID and user information, second line is user ID and user query. You can use code snippet like following to retrive data and store them as a two dimensional array.

file = open("wordprocessed.txt")
fileget = file.read().split("\n")
userInfo = eval(fileget[0])
queryList = eval(fileget[1])
=======
zh.json is stop word list, sougou.dic is a Chinese word tag dictionary, both are used to improve word segmentation accuracy.
>>>>>>> origin/master
=======
zh.json is stop word list, sougou.dic is a Chinese word tag dictionary, both are used to improve word segmentation accuracy.
>>>>>>> origin/master
