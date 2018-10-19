# Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
#
# Example 1:
#
#
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#
#
# Example 2:
#
#
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#
#
# Note:
#
#
# 	The relative order inside both the even and odd groups should remain as it was in the input.
# 	The first node is considered odd, the second node even and so on ...
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head
        even = head
        odd = head.next
        odd_start = head.next
        while even or odd:
            if even:
                if even.next:
                    even.next = even.next.next
                    if even.next is None:
                        even.next = odd_start
                        break
                    even = even.next
                else:
                    even.next = odd_start
                    break
            if odd:
                if odd.next:
                    odd.next = odd.next.next
                    odd = even.next
        return head
            
        
        
