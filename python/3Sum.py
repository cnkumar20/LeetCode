#Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

#Note: The solution set must not contain duplicate triplets.

#For example, given array S = [-1, 0, 1, 2, -1, -4],

#A solution set is:
#[
  #[-1, 0, 1],
  #[-1, -1, 2]
#]

def Sum3(input_arr):
    temparr = []
    index = dict()
    for x in input_arr:
        index[-x] = 1
        print(-x)
    for i in range(len(input_arr)):
        for j in range(1,len(input_arr)):
            sum = input_arr[i]+input_arr[j]
            if(index.has_key(sum)):
                temparr.append([input_arr[i],input_arr[j],-sum])
    return temparr
print(Sum3([-1, 0, 1, 2, -1, -4]))