# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if(root == None):
            return 0
        if(root!=None):
            leftd = self.maxDepth(root.left)
            rightd = self.maxDepth(root.right)
            if(leftd > rightd):
                return leftd+1
            else :
                return rightd+1
