# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        # recursion approach
        # if(head == None): 
        #     return head;
        # if(head.val == val): 
        #     return self.removeElements(head.next, val);
        # head.next = self.removeElements(head.next, val)
        # return head
        
        if head is None:
            return head
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return None
        
        prev = head
        curr = head.next
        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head
        
        
