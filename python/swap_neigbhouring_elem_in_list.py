#swap neighbohouring element in the list
#[1,2,3,4,5] ---> result  [2,1,4,3,5]

def findParenthesisDepth(elementList):
 resultList = list()   
 if(len(elementList)==1):
    resultList.append(elementList[0])
    return resultList
 for x in range(1,len(elementList),2): 
    resultList =  resultList + [elementList[x],elementList[x-1]]
 if(len(elementList)%2!=0):
    print("aaa")
    resultList.append(elementList[x+1])
 return resultList
 
print(findParenthesisDepth([1,2,3]))
