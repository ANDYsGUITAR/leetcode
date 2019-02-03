# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
#   [15,7],
#   [9,20],
#   [3]
# ]
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans
        stack = [root]
        while stack:
            temp = []
            l = len(stack)
            for _ in range(l):
                node = stack.pop(0)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                temp.append(node.val)
            ans.append(temp)
        ans.reverse()
        return ans
                
