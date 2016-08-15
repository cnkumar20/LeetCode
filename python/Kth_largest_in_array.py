import Queue as Q
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = Q.PriorityQueue()

        for x in nums:
            q.put(x)
            if(q.qsize() > k):
                q.get()
        return q.get()