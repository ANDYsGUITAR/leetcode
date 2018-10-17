# Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
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
# return its level order traversal as:
#
# [
#   [3],
#   [9,20],
#   [15,7]
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res =[]
        if root is None:
            return []
        q = []
        q.append(root)
        while (len(q)) != 0:
            tmp = []
            length = len(q)
            for i in range(length):
                r = q.pop(0)
                if r.left is not None:
                    q.append(r.left)
                if r.right is not None:
                    q.append(r.right)
                tmp.append(r.val)
            res.append(tmp)
        return res
        
