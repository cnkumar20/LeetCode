def mergeSort(a):
    if(len(a)>1):
	//hammer
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while(i < len(lefthalf) and j < len(righthalf)):
            if(lefthalf[i]<righthalf[j]):
               a[k] = lefthalf[i]
               i +=1
            else:
               a[k] = righthalf[j]
               j +=1
            k +=1
        while(i<len(lefthalf)):
            a[k]=lefthalf[i]
            i +=1
            k +=1
        while(j<len(righthalf)):
            a[k] = righthalf[j]
            j+=1
            k+=1
    print("Merging--",a)


ab = [3,2,4,6,2,6,7,2,1,65,5]
mergeSort(ab)
print(ab)

