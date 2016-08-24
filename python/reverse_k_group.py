
#Reverse the array elements by group of k
#([1,2,3,4,5,6,7,8,9],3)
#[3, 2, 1, 6, 5, 4, 9, 8, 7] 
def reverse_k_group(nList,k):
    a = []
    for x in range(0,len(nList),k):
        temp = nList[x:x+k]
        temp.reverse()
        a.extend(temp)
     #   a.append(nList)
    return a
    
print(reverse_k_group([1,2,3,4,5,6,7,8,9],3))
