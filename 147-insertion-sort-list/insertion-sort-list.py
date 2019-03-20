# Sort a linked list using insertion sort.
#
#
#
#
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
#  
#
#
#
#
# Algorithm of Insertion Sort:
#
#
# 	Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# 	At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# 	It repeats until no input elements remain.
#
#
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
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        toInsert = head
        while head and head.next:
            if head.val > head.next.val:
                toInsert = head.next
                prevInsert = dummy
                while prevInsert.next.val < toInsert.val:
                    prevInsert = prevInsert.next
                head.next = toInsert.next
                toInsert.next = prevInsert.next
                prevInsert.next = toInsert
            else:
                head = head.next
        return dummy.next
                
        # l = []
        # node = head
        # while node:
        #     l.append(node.val)
        #     node = node.next
        # n = len(l)
        # for i in range(1, n):
        #     if l[i] < l[i - 1]:
        #         j = i - 1
        #         while j >= 0 and l[j] > l[i]:
        #             j -= 1
        #         l = l[: j + 1] + [l[i]] + l[j + 1 : i] + l[i + 1:]
        # node = head
        # for i in range(n):
        #     node.val = l[i]
        #     node = node.next
        # return head
        
