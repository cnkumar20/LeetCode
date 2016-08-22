class Solution(object):

    def lexicalOrder(self, n):

        """

        :type n: int

        :rtype: List[int]

        """
        result=list([1])
        unit = 1
        if(n == 1):
           result.append(1)
           return result

        while(len(result)<n):

           if(result[-1]*10 <= n):
                result.append(result[-1]*10)
                continue

           elif(result[-1]+1<= n and int(str(result[-1]+1)[0]) <= unit):
                result.append(result[-1]+1)
                continue

           else:
               if(not int(str(result[-1]+1)[0])<=unit):
                  unit += 1
               num = result[-1]
               num = num/10
               num = num +1
               result.append(num)

        return result

a = Solution()
print(a.lexicalOrder(100))
