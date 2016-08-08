class Solution:

    def __init__(self):
        self.integer = 0
        self.reverseInteger = 0

    def readInteger(self):
        print("Enter the nuber :")
        self.integer = int(input())
    def calculate(self):
        self.readInteger()
        a  = self.integer
        while(a/10!=0):
            tmp = a%10
            if(tmp !=0):
                self.reverseInteger = self.reverseInteger*10 + tmp
            else:
                self.reverseInteger = self.reverseInteger*10
            a = a/10
        self.reverseInteger = self.reverseInteger*10 + a%10
        print("Reversed integer :",self.reverseInteger)

test = Solution()
test.calculate()