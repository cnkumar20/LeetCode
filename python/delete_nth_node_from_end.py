# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: inte
        :rtype: ListNode
        """
        listLength = 0
        if(head == None):
            return None
        temp = head
        while(temp != None):
            temp = temp.next
            listLength +=1

        if(n > listLength):
            return head

        if(listLength == n):
            head = head.next
            return head


        cur = head
        temp = None

        for x in range(listLength-n):
            temp = head
            head = head.next

        head = head.next
        temp.next = head

        return cur