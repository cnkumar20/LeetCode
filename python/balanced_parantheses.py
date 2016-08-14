class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)%2 != 0):
            return False
        l1 = list(s)
        resultList = list()
        for x in l1:
            if(len(resultList)==0):
                resultList.extend(x)
                continue

            if(resultList[len(resultList)-1] == '(' and x == ')'):
                resultList.pop()

            elif(resultList[len(resultList)-1] == '{' and x == '}'):
                resultList.pop()

            elif(resultList[len(resultList)-1] == '[' and x == ']'):
                resultList.pop()
            else:
                resultList.extend(x)

        if(len(resultList)==0):
            return True
        else:
            return False