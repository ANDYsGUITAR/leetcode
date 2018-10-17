# Given a linked list, remove the n-th node from the end of list and return its head.
#
# Example:
#
#
# Given linked list: 1->2->3->4->5, and n = 2.
#
# After removing the second node from the end, the linked list becomes 1->2->3->5.
#
#
# Note:
#
# Given n will always be valid.
#
# Follow up:
#
# Could you do this in one pass?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        length = 1
        p = head
        t = head
        if p.next is None:
            return None
        while p.next:
            length += 1
            p = p.next
        print(length)
        count = 1
        if length+1-n == 1:
            head = head.next
            return head
        if length+1-n == 2:
            t.next = t.next.next
            return head
        while count < length-n:
            t = t.next
            count += 1
        t.next = t.next.next
        return head
        
        
        
