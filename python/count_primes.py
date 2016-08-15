class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n==0 or n==1 or n==2):
            return 0
        a = [True]*n
        a[0] = False
        a[1] = False

        for x in range(2,int(math.sqrt(n))+1):
            if(a[x]):
                for i in range(x+x,n,x):
                    a[i] = False
        return a.count(True)

