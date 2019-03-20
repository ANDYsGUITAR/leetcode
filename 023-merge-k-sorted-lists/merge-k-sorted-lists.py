# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
# Example:
#
#
# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: 'List[ListNode]') -> 'ListNode':
        vals = []
        for node in lists:
            while node:
                vals.append(node.val)
                node = node.next
        vals.sort()
        head = ListNode(0)
        node = head
        for v in vals:
            tmp = ListNode(v)
            node.next = tmp
            node = tmp
        return head.next
            
