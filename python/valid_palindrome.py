class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = list(s)
        string = [x for x in string if(str(x).isalpha() or str(x).isalnum())]
        
        i =0
        j = len(string)-1
        while(i <= j):
            if(str(string[i]).lower()!=str(string[j]).lower()):
                return False
            i +=1
            j -=1
        return True
        
test = Solution()
print(test.isPalindrome("A man,a plan, a canal: Panama"))
