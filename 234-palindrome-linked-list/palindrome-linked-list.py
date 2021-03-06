# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        # print(slow.val, rev.val)
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev
        # O(N)space
#         if head is None:
#             return True
#         if head.next is None:
#             return True
#         s = []
#         p = head
#         while not p is None:
#             s.append(p.val)
#             p = p.next
#         if s == s[::-1]:
#             return True
#         else:
#             return False
        
