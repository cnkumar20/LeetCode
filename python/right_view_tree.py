# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(root == None):
            return []
        if(root.left == None and root.right == None):
            return root


        result = list()

        q = collections.deque()

        q.extend([root])

        while(len(q)!=0):
            result.extend([q[len(q)-1].val])
            index = len(q)
            for x in range(index):
                node = q.popleft()
                if(node.left != None):
                    q.extend([node.left])
                if(node.right != None):
                    q.extend([node.right])
        return result


