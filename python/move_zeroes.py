def moveZeroes(inputNums):
    j = 0
    for i,c in enumerate(inputNums):
         if(c != 0):
                inputNums[i],inputNums[j] = inputNums[j],inputNums[i]
                j +=1
a1 = [0, 1, 0, 3, 12]
moveZeroes(a1)
print(a1)
