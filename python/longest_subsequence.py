class Solution(object):

    def lengthOfLIS(self, nums):

        """

        :type nums: List[int]

        :rtype: int

        """

        #[3,1,2,5,6,4,7]

        dp = [1]*len(nums)

        for i in range(len(nums)):

            for j in range(i):

                if(nums[j] < nums[i]):

                    dp[i] = max(dp[i],dp[j]+1)

        return max(dp) if dp else 0

test = Solution()
print(test.lengthOfLIS([-2,-1,1,0,4,2,1]))
