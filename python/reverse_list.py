class Node():
    def __init__(self,data):
        #super(Node, self).__init__()
        self.data = data
        self.next = None
class ListFunction():

    def __init__(self, node):
        #super(ListFunction, self).__init__()
        self.head = node
    def addFront(self,node1):
        node1.next = self.head
        self.head = node1
    def addLast(self,node1):
        node = self.head
        while(node.next != None):
            node = node.next
        node.next = node1
    def reverse(self):
       cur = self.head
       temp = None
       prev = None
       while(cur.next != None):
           prev = cur
           cur = cur.next
           prev.next = temp
           temp = prev
       cur.next = prev
       self.head = cur
    def printList(self):
        cur = self.head
        while(cur != None):
            print(cur.data," ",end="")
            cur = cur.next
            print()

test_list = ListFunction(Node(1))
test_list.addLast(Node(2))
test_list.addLast(Node(3))
test_list.addLast(Node(4))
test_list.printList()
test_list.reverse()
test_list.printList()