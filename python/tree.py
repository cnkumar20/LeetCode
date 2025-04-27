class Node():
    def __init__(self,d):
        self.data = d
        self.left  = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None
    
    def _insert(self,cur,node):
        if(node.data < cur.data):
            cur.left = node if not cur.left else self._insert(cur.left,node)
        else:
            cur.right = node if not cur.right else self._insert(cur.right,node)
    
    def insert(self,node):
        if not self.root:
            self.root = node
            return
        self._insert(self.root,node)
