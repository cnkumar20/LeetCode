# Definition for a binary tree node.

# class TreeNode(object):

#     def __init__(self, x):

#         self.val = x

#         self.left = None

#         self.right = None



class Solution(object):

        def isSymmetric(self,root):

                if(root is None) :

                        return True

                return self.isSymmetricRecursion(root.left, root.right)

        def isSymmetricRecursion(self,left,right):

                if(left is None and right is None):

                        return True

                if(left is None or right is None or left.val!=right.val):

                        return False

                return (self.isSymmetricRecursion(left.left,right.right) and self.isSymmetricRecursion(left.right,right.left))


