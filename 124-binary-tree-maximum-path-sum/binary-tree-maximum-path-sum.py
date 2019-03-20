# Given a non-empty binary tree, find the maximum path sum.
#
# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
#
# Example 1:
#
#
# Input: [1,2,3]
#
#        1
#       / \
#      2   3
#
# Output: 6
#
#
# Example 2:
#
#
# Input: [-10,9,20,null,null,15,7]
#
#    -10
#    / \
#   9  20
#     /  \
#    15   7
#
# Output: 42
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = float('-inf')
        def helper(root):
            if not root:
                return 0
            l = max(0, helper(root.left))
            r = max(0, helper(root.right))
            self.ans = max(self.ans, l + r + root.val)
            return root.val + max(l, r)
        helper(root)
        return self.ans
