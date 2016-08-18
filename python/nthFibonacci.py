"""
Problem Statement
=================
Given the number n, find the nth fibanacci number.
The fibonacci series is 0, 1, 1, 2, 3 ...
And follows the formula Fn = Fn-1 + Fn-2
Complexity
----------
* Recursive Solution: O(2^n)
* Dynamic Programming: O(n)
"""

def nthFibonacci(n):
    memList = [0]*(n+1)
    memList[0] = 1
    if(n==0 or n==1):
        return n
    memList[0] = 1
    memList[1] = 1
    for x in range(2,n+1):
        memList[x] = memList[x-2]+memList[x-1]
    return memList[n]

print(nthFibonacci(4))

