# Reverse a singly linked list.
#
# Example:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
#
#
# Follow up:
#
# A linked list can be reversed either iteratively or recursively. Could you implement both?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if not head.next:
            return head
        p = head
        q = head.next
        p.next = None
        while q.next:
            r = q.next
            q.next = p
            p = q
            q = r
        q.next = p
        return q

            
