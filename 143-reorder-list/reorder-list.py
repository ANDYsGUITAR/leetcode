# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#
#
# Given 1->2->3->4, reorder it to 1->4->2->3.
#
# Example 2:
#
#
# Given 1->2->3->4->5, reorder it to 1->5->2->4->3.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return None
        node = head
        l = []
        while node:
            l.append(node)
            node = node.next
        node = head
        count = len(l) // 2
        if len(l) % 2 == 1:
            for i in range(1, count + 1):
                l[-i].next = node.next
                l[-i-1].next = None
                node.next = l[-i]
                node = node.next.next
        else:
            for i in range(1, count):
                l[-i].next = node.next
                l[-i-1].next = None
                node.next = l[-i]
                node = node.next.next
        

            
