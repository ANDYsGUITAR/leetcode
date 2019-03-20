# Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
#
# Example 1:
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
#
# Example 2:
#
#
# Input: 1->1->1->2->3
# Output: 2->3
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: 'ListNode') -> 'ListNode':
        dummy = ListNode(0)
        dummy.next = head
        node = head
        prev = dummy
        while node and node.next:
            if node.val == node.next.val:
                while node and node.next and node.val == node.next.val:
                    node = node.next
                node = node.next
                prev.next = node
            else:
                prev = prev.next
                node = node.next
        return dummy.next
