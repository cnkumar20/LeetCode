def isSubsetSumRec(arr,sum_value,n):
    if(sum_value==0):
        return True
    if(n==0):
        return False
    if arr[n-1] > sum_value:
        return isSubsetSumRec(arr,sum_value,n-1)
    return isSubsetSumRec(arr,n-1,sum_value-arr[n-1]) or isSubsetSumRec(arr,n-1,sum_value)


def isSubsetSum(arr,sum_value):
    n = len(arr)
    isSubsetSumRec(arr,sum_value,n)

def isSubsetSumMemoization(arr,sum_value,memo,n):
    if sum_value==0:
        return True
    if n<=0:
        return False
    if memo[n][sum_value] != -1:
        return memo[n][sum_value]
    if(arr[n-1] > sum_value):
        memo[n][sum_value] = isSubsetSumMemoization(arr,sum_value-arr[n-1],memo,n-1) or isSubsetSumMemoization(arr,sum_value,memo,n-1)
    return memo[n][sum_value]



if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    sum_value = 9

    if isSubsetSum(arr, sum_value):
        print("True")
    else:
        print("False")
