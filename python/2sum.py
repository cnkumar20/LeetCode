#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution.
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = dict()
        count = 0
        for n in nums:
            result[target-n] = count
            count +=1
        count = 0
        for x in nums:
            if(result.has_key(x)):
                return [result[x],count]
            count +=1
a = [1,2,3,4,1,4]
ab = Solution()
print(ab.twoSum(a,5))

