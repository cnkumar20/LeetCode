class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def reverseString(self, string):
    # Write your code here
        string = list(string)
        for x in range(len(string)-1,int(len(string)/2-1),-1):
            temp = string[x]
            string[x] = string[len(string)-x-1]
            string[len(string)-x-1] = temp
        return "".join(string)
    
    def reverseString1(self,string):
    # Write your code here
        string = list(string)
        string.reverse()
        return "".join(string)
    
    
