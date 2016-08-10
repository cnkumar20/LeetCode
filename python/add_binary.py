class Solution(object):
    def addBinary(self, a, b):
        ip1 = list(a)
        ip2 = list(b)
        ip1.reverse()
        ip2.reverse()
        
        length = len(ip1) if len(ip1) < len(ip2) else len(ip2)
        carry = 0
        sum1 = list()
        index = 0
        
        for i in range(length):
               sum1.extend(str((carry+int(ip1[i])+int(ip2[i]))%2))
               carry = (carry+int(ip1[i])+int(ip2[i]))//2
               index = i 
                
                
        index +=1
        
        if(len(ip1)<len(ip2)):
            while(index < len(ip2)):
                sum1.extend(str((carry+int(ip2[index]))%2))
                carry = (carry+int(ip2[index]))//2
                index +=1
        else:
            while(index < len(ip1)):
                sum1.extend(str((carry+int(ip1[index]))%2))
                carry = (carry+int(ip1[index]))//2
                index +=1
        if(carry==1):
            sum1.extend(str(carry))
        sum1.reverse()
        return  "".join(sum1)
                
            
                
                
            
        
        
test = Solution()
print(test.addBinary("11","11"))
