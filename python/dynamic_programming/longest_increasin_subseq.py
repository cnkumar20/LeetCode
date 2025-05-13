def lisEnding(arr,idx):
    if(idx==0):
        return 1
    mx = 1
    for prev in range(idx):
        if arr[prev] < arr[idx]:
            mx = max(mx,lisEnding(arr,prev)+1)
    return mx

def lis(arr):
    n = len(arr)
    res = 1
    for idx in range(1,n):
        res = max(res,lisEnding(arr,idx)+1)

if __name__ == "__main__":
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    print(lis(arr))
