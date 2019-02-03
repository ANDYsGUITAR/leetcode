# Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.
#
# Example:
#
#
# Input:
#
#    1
#     \
#      3
#     /
#    2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
#
#
#  
#
# Note: There are at least two nodes in this BST.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.prev = None
        self.ans = float('inf')
        self.inorder(root)
        return self.ans
        
        
        
    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        if self.prev:
            self.ans = min(self.ans, root.val - self.prev.val)
        self.prev = root
        self.inorder(root.right)
