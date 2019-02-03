# Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.
#
#
#
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
#
# Two binary trees are considered leaf-similar if their leaf value sequence is the same.
#
# Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
#
#  
#
# Note:
#
#
# 	Both of the given trees will have between 1 and 100 nodes.
#
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        list1 = []
        list2 = []
        self.leaf(root1, list1)
        self.leaf(root2, list2)
        return list1 == list2
        
    def leaf(self, root, leaf_list):
        if root is None:
            return
        elif root.left is None and root.right is None:
            leaf_list.append(root.val)
        else:
            self.leaf(root.left, leaf_list)
            self.leaf(root.right, leaf_list)
