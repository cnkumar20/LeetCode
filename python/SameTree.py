class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if(p!=None & q!=None):
            if(p.val != q.val):
                return False
            if(isSameTree(p.left,q.left) & isSameTree(p.right,q.right)):
                return True
        if(p==None^q==None):
            return False
        else:
            return True
a = Solution()
a.isSameTree([],[])