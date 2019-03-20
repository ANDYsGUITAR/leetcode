# Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
#
# You should preserve the original relative order of the nodes in each of the two partitions.
#
# Example:
#
#
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: 'ListNode', x: 'int') -> 'ListNode':
        left = ListNode(0)
        p1 = left
        right = ListNode(0)
        p2 = right
        node = head 
        while node:
            if node.val < x:
                p1.next = ListNode(node.val)
                p1 = p1.next
            else:
                p2.next = ListNode(node.val)
                p2 = p2.next
            node = node.next
        p1.next = right.next
        return left.next
        
