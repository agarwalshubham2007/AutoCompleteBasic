from collections import OrderedDict
from Model import dicRoot
from Model import dataDictionary
import operator

def searchEngine(inp):
    global dataDictionary

    inp = inp.lower()
    if inp == "":
        print "Please enter a search term"
    else:
        tempDic = dicRoot

        # search at each level
        for index in range(len(inp)):
            if tempDic.has_key(inp[index]):
                tempDic = tempDic[inp[index]]
            else:
                return "No Results"

        resultDict = {}
        dataDictionary = OrderedDict(sorted(dataDictionary.items()))
        for x in range(tempDic['Result'][0], tempDic['Result'][1]+1):
            resultDict[dataDictionary.keys()[x]] = dataDictionary.values()[x]

        sorted_result = sorted(resultDict.items(), key=operator.itemgetter(1),reverse=True)

        output = ""
        result_num=10
        for item in sorted_result:
            if result_num>=1:
                output = output+ item[0]+" <br> "
            else:
                break
            result_num-=1

        return output