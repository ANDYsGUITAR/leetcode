# -*- coding:utf-8 -*-


# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
#    1
#     \
#      2
#     /
#    3
#
# Output: [1,2,3]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        result = []
        stack = []
        node = root
        while node or stack:
            while node:
                result.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return result
#         result = []
#         self.recursion(root, result)
#         return result
        
#     def recursion(self, root, result):
#         if root is None:
#             return
#         result.append(root.val)
#         self.recursion(root.left, result)
#         self.recursion(root.right, result)
        
        
