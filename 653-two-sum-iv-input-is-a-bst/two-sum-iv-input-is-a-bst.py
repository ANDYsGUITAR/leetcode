# Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
#
# Example 1:
#
#
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 9
#
# Output: True
#
#
#  
#
# Example 2:
#
#
# Input: 
#     5
#    / \
#   3   6
#  / \   \
# 2   4   7
#
# Target = 28
#
# Output: False
#
#
#  
#


class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        # using hashset
        s = set()
        return self.find(root, k, s)
        
        
    def find(self, root, k, s):
        if root is None:
            return False
        if k - root.val in s:
            return True
        else:
            s.add(root.val)
            return self.find(root.left, k, s) or self.find(root.right, k, s)
