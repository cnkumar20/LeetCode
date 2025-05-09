class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        pass
    

    def maxPath(self,node):
        if(node == None):
            return 0
        left = self.maxPath(node.left) if(node.left != None )  else  -9999
        right = self.maxPath(node.right) if(node.right!= None) else -9999
        return max(left,right)+node.val

