from collections import OrderedDict
import os

dataDictionary = {} # array storing data, sorted by words
dicRoot = {} # this is root of tree dictionary data structure

def autoCompleteTrain():
    global dataDictionary, dicRoot

    root_path = os.path.dirname(os.path.realpath(__file__))
    final_path = root_path +  "/Data/data.csv"

    # loading csv file into dictionary with key as words and value as scores
    with open(final_path, "r") as file:
        for line in file:
            l = line.split(',')
            l[1] = l[1].replace("\n","")
            dataDictionary[l[0].lower()] = l[1]
    print dataDictionary
    # sorting the dictionary by words(keys) alphabetically increasing
    dataDictionary = OrderedDict(sorted(dataDictionary.items()))

    item_num = 0 # index of word in dataDictionary

    # formation of tree hashmap data structure with at most 5 levels of height!
    for item_word, item_score in dataDictionary.iteritems():
        tempDic = dicRoot
        level=1
        for index in range(len(item_word)):
            if level<=5:
                if tempDic.has_key(item_word[index]):
                    tempDic[item_word[index]]['Result'][1] += 1
                    tempDic=tempDic[item_word[index]]
                else:
                    tempDic[item_word[index]] = {}
                    tempDic[item_word[index]]['Result'] = [item_num,item_num]
                    tempDic = tempDic[item_word[index]]
                level+=1
            else:
                break

        item_num += 1




