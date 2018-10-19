# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
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
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or len(postorder) == 0:
            return None
        
        root = TreeNode(postorder[-1])
        root_index = inorder.index(postorder[-1])
        
        del postorder[-1]
        
        left_post = postorder[:root_index]
        right_post = postorder[root_index:]
        
        left_in = inorder[:root_index]
        right_in = inorder[root_index + 1:]

        root.left = self.buildTree(left_in,left_post)
        root.right = self.buildTree(right_in,right_post)
        
        return root
