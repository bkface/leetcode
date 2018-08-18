# https://leetcode.com/problems/merge-k-sorted-lists/description/

from heapq import heappush, heappop, heapify

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        tail = head
        
        heap = []
        for i, n in enumerate(lists):
            if n is not None:
                heap.append((n.val, i, n))
        heapify(heap)

        while heap:
            _, i, n = heappop(heap)
            tail.next = n
            tail = tail.next
            n = n.next
            if n is not None:
                heappush(heap, (n.val, i, n))
        return head.next
