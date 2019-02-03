# -*- coding:utf-8 -*-


# Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#
# Calling next() will return the next smallest number in the BST.
#
#  
#
#
#
#
# Example:
#
#
#
#
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
#
#
#  
#
# Note:
#
#
# 	next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
# 	You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
#
#


# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        result = []
        self.inOrder(root,result)
        self.inOrderData = result
    
    def inOrder(self, root, result):
        if root is None:
            return
        self.inOrder(root.left, result)
        result.append(root.val)
        self.inOrder(root.right, result)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.inOrderData) > 0
        

    def next(self):
        """
        :rtype: int
        """
        return self.inOrderData.pop(0)
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
