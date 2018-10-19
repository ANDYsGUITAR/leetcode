# -*- coding:utf-8 -*-


# Given a binary tree, return the postorder traversal of its nodes' values.
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
# Output: [3,2,1]
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
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        myStack1 = []
        myStack2 = []
        result = []

        node = root
        myStack1.append(node)
        while myStack1:
        # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.left:
                myStack1.append(node.left)
            if node.right:
                myStack1.append(node.right)
            myStack2.append(node)
        while myStack2:
        # 将myStack2中的元素出栈，即为后序遍历次序
            result.append(myStack2.pop().val)
        return result
            
#         result = []
#         self.recursion(root,result)
#         return result
    
#     def recursion(self,root,result):
#         if root is None:
#             return
#         self.recursion(root.left,result)
#         self.recursion(root.right,result)
#         result.append(root.val)
