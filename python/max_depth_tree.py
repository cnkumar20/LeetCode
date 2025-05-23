from Node import Node

class Solution:
    def find_max_depth(self,r):
        if r==None:
            return -1
        left = self.find_max_depth(r.left)
        right = self.find_max_depth(r.right)
        return max(left,right)+1
        
