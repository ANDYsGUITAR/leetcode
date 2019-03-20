# Sort a linked list in O(n log n) time using constant space complexity.
#
# Example 1:
#
#
# Input: 4->2->1->3
# Output: 1->2->3->4
#
#
# Example 2:
#
#
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        l = []
        node = head
        while node:
            l.append(node.val)
            node = node.next
        l.sort()
        node = head
        for i in range(len(l)):
            node.val = l[i]
            node = node.next
        return head
