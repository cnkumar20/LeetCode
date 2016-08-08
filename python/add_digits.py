class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        x = num
        result = 0
        while(x/10!=0):
            digit = x%10
            result += digit
            x = int(x/10)
        if(x!=0):
            result += x
        if(result > 9):
            return self.addDigits(result)
        return result
a = Solution()
print(a.addDigits(10))
