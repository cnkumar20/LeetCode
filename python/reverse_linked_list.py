# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        if(cur==None or cur.next == None):
            return cur
        prev = cur
        cur = cur.next
        prev.next = None
        while(cur!=None):
            temp = prev
            prev = cur
            cur = cur.next
            prev.next = temp
        return prev
