def merge_dictionaries(dict1,dict2):
    mergedDictionary= dict1.copy()
    for key,value in dict2.items():
        mergedDictionary[key]=value
    return mergedDictionary


