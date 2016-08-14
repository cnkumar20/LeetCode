class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        i=0
        j=len(matrix)-1
        while(i < len(matrix[0]) and j >= 0):
                if(matrix[j][i]==target):
                    return True
                elif(matrix[j][i] > target):
                    j -=1
                else:
                    i +=1
        return False
