class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return None
        if(len(nums)==1):
            return nums[0]
        ans = [0]*len(nums)
        max1 = nums[0]
        ans[0] = nums[0]
        for x in range(1,len(nums)):
            ans[x] = max(nums[x],ans[x-1]+nums[x])
            max1 = max(max1,ans[x])
        return max1
