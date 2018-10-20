# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
#
# Return the following binary tree:
#
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root = TreeNode(preorder[0])
        r_index = inorder.index(preorder[0])
        
        del preorder[0]
        
        left_pre = preorder[:r_index]
        right_pre = preorder[r_index:]
        
        left_in = inorder[:r_index]
        right_in = inorder[r_index+1:]
        
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre,right_in)
        
        return root
