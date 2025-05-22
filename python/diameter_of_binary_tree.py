class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Solution:
    def findDiameterRecur(self,root,res) -> int:
        if root is None:
            return 0 
        left = self.findDiameterRecur(root.left,res)
        right = self.findDiameterRecur(root.right,res)
        res[0] = max(res[0],left+right)
        return 1+max(left,right)

    def findDiameter(self,tree:Node):
        res = [0]
        res = self.findDiameterRecur(tree,res)

