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
		return self.isSymmetricRecu(left.left,right,right) and self,isSymmetricRecu(left.right,right.left)

