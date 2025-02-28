#First Question
# def merge_dictionaries(dict1,dict2):
#     mergedDictionary= dict1.copy()
#     for key,value in dict2.items():
#         mergedDictionary[key]=value
#     return mergedDictionary
# dict1 = {"a":1,"b":2,"c":3}
# dict2 = {"b":10,"d":4}
# print(merge_dictionaries(dict1,dict2))


#Second Question
sentence=input("Please enter any sentence: ")
wordNumbsDict={}
words=sentence.split()
for i in words:
    if i in wordNumbsDict:
        wordNumbsDict[i]+=1
    else:
        wordNumbsDict[i]=1
print(wordNumbsDict)

    
    






