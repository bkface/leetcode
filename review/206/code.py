# https://leetcode.com/problems/reverse-linked-list/description/

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
        if head is None:
            return head
        ans = ListNode(head.val)
        while(head.next is not None):
            tmp = ans
            ans = ListNode(head.next.val)
            ans.next = tmp
            head = head.next
        return ans
        
