# -*- coding:utf-8 -*-


# Given a linked list, rotate the list to the right by k places, where k is non-negative.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
#
#
# Example 2:
#
#
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
#


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        k = k%length
        # print(length)
        if k == 0:
            return head
        cur = head
        tail = head
        i = 0
        while i != length - 1:
            cur = cur.next
            i += 1
        cur.next = head
        i = 0
        while i != length - 1 - k:
            tail = tail.next
            i += 1
        head = tail.next
        tail.next = None
        return head
        
        
