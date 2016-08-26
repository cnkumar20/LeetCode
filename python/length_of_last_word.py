class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for x in s[::-1]:
            if('z' >= x >= 'a' or 'Z' >= x >= 'A'):
                result += 1
                flag = True
            elif(result!=0):
                break

        return result