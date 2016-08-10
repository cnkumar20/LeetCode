#[1] , [0], [] = return as it is
#[1,0]
#[0,1]
def anagrams(test,original):
    a = dict();
    for x in list(original):
        if(x in a):
            a[x] +=1
        else :
            a[x] = 1
    for x in list(test):
        if(x not in a ):
            return False
        else:
            a[x] -= 1
    for i in a:
        if(a[i] != 0):
            return False
    return True
    
print(anagrams("Kumar","Kumar"))
