# Given an n-ary tree, return the postorder traversal of its nodes' values.
#
# For example, given a 3-ary tree:
#
#  
#
#
#
#  
#
# Return its postorder traversal as: [5,6,3,2,4,1].
#  
#
# Note:
#
# Recursive solution is trivial, could you do it iteratively?
#


"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans = []
        if root is None:
            return ans
        def recursion(root, ans):
            for children in root.children:
                recursion(children, ans)
            ans.append(root.val)
        recursion(root, ans)
        return ans
