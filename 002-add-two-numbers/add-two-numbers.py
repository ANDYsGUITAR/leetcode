# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headVal = (l1.val+l2.val)%10
        if l1.val+l2.val >= 10:
            carry = 1
        else:
            carry = 0
        head = ListNode(headVal)
        cur = head
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            val = carry + l1.val + l2.val
            if val >= 10:
                carry = 1
            else:
                carry = 0
            newNode = ListNode(val%10)
            cur.next = newNode
            cur = newNode
            l1 = l1.next
            l2 = l2.next
        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        else:
            if carry == 1:
                newNode = ListNode(1)
                cur.next = newNode
                return head
            else:
                return head
        if l1:
            while l1 and carry == 1:
                val = carry + l1.val
                if val >= 10:
                    carry = 1
                else:
                    carry = 0
                l1.val = val%10
                if l1.next == None and carry == 1:
                    newNode = ListNode(1)
                    l1.next = newNode
                    return head
                l1 = l1.next
            return head
        if l2:
            while l2 and carry == 1:
                val = carry + l2.val
                if val >= 10:
                    carry = 1
                else:
                    carry = 0
                l2.val = val%10
                if l2.next == None and carry == 1:
                    newNode = ListNode(1)
                    l2.next = newNode
                    return head
                l2 = l2.next
            return head
        
        
        
