# -*- coding:utf-8 -*-


# Given a binary tree
#
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
#  
#
# Example:
#
#
#
#
# Input: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":null,"right":null,"val":4},"next":null,"right":{"$id":"4","left":null,"next":null,"right":null,"val":5},"val":2},"next":null,"right":{"$id":"5","left":null,"next":null,"right":{"$id":"6","left":null,"next":null,"right":null,"val":7},"val":3},"val":1}
#
# Output: {"$id":"1","left":{"$id":"2","left":{"$id":"3","left":null,"next":{"$id":"4","left":null,"next":{"$id":"5","left":null,"next":null,"right":null,"val":7},"right":null,"val":5},"right":null,"val":4},"next":{"$id":"6","left":null,"next":null,"right":{"$ref":"5"},"val":3},"right":{"$ref":"4"},"val":2},"next":null,"right":{"$ref":"6"},"val":1}
#
# Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B.
#
#
#  
#
# Note:
#
#
# 	You may only use constant extra space.
# 	Recursive approach is fine, implicit stack space does not count as extra space for this problem.
#


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        head = None # head of the next level
        prev = None # the leading node of the next level
        cur = root # current node of current level
        
        while cur != None:
            while cur != None: # iterate on the current level
                if cur.left != None:
                    if prev != None:
                        prev.next = cur.left
                    else:
                        head = cur.left
                    prev = cur.left
                if cur.right != None:
                    if prev != None:
                        prev.next = cur.right
                    else:
                        head = cur.right
                    prev = cur.right
                cur = cur.next
            cur = head
            head = None
            prev = None
            
