# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
        def hasPathSum(self, root, sum):
            """
            :type root: TreeNode
            :type sum: int
            :rtype: bool
            """
            cur = 0
            return self.check(root,cur,sum)

        def check(self,root,cur,sum):
            if(root == None):
                return False
            if(root.left == None and root.right == None):
                if(cur+root.val == sum):
                    return True
            if(root.left != None or root.right != None):
                return self.check(root.left,cur + root.val,sum) or self.check(root.right,cur + root.val,sum)
            return False
