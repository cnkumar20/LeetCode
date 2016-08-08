#Given an array of integers, every element appears twice except for one. Find that single one.
class Solution(object):

    def __init__(self):
        pass

    def singleNumber(self,A):
        xst = 0
        for i in A:
            xst ^= i
            return xst
inputStr = input()
sol = Solution()

print(sol.singleNumber(inputStr))