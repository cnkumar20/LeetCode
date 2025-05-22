class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return 
        if(root.data == p or root.data == q):
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root

        return left if left else right
