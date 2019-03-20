# Given a linked list, swap every two adjacent nodes and return its head.
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
#  
#
# Example:
#
#
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: 'ListNode') -> 'ListNode':
        # vals = []
        # node = head
        # while node:
        #     vals.append(node.val)
        #     node = node.next
        # node = new = ListNode(0)
        # if len(vals) == 1:
        #     return head
        # if len(vals) == 0:
        #     return new.next
        # for i in range(0, len(vals), 2):
        #     if i + 1 < len(vals):
        #         vals[i], vals[i + 1] = vals[i + 1], vals[i]
        # for v in vals:
        #     tmp = ListNode(v)
        #     node.next = tmp
        #     node = tmp
        # return new.next
        
        prev, prev.next = ListNode(0), head
        dummy = prev
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            prev.next, a.next, b.next = b, b.next, a
            prev = a
        return dummy.next
