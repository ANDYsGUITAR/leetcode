# -*- coding:utf-8 -*-


#
# Given a linked list, determine if it has a cycle in it.
#
#
#
# Follow up:
# Can you solve it without using extra space?
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False
        slow = head.next
        if slow is None:
            return False
        fast = slow.next
        
        while slow and fast:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
        return False
        
