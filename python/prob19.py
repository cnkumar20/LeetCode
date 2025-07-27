# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_stack = deque()
        node = head
        while(node != None):
            temp_stack.append(node)
            node = node.next
        i = 0
        prev= None
        cur = None
        while(i != n):
            prev = cur
            cur = temp_stack.pop()
            i += 1
        if(prev==None and len(temp_stack)==0):
            return None
        if(len(temp_stack)==0):
            return prev
        if(i==n):
            cur = temp_stack.pop()
            cur.next = prev
        return head 
