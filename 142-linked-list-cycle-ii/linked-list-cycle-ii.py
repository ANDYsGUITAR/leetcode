# -*- coding:utf-8 -*-


#
# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
#
#
#
# Note: Do not modify the linked list.
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
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeSet = set()
        if head is None:
            return None
        while True:
            if head in nodeSet:
                return head
            else:
                nodeSet.add(head)
                if head.next == None:
                    return None
                head = head.next
        
        
        
