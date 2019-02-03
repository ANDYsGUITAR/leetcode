# We want to use quad trees to store an N x N boolean grid. Each cell in the grid can only be true or false. The root node represents the whole grid. For each node, it will be subdivided into four children nodes until the values in the region it represents are all the same.
#
# Each node has another two boolean attributes : isLeaf and val. isLeaf is true if and only if the node is a leaf node. The val attribute for a leaf node contains the value of the region it represents.
#
# Your task is to use a quad tree to represent a given grid. The following example may help you understand the problem better:
#
# Given the 8 x 8 grid below, we want to construct the corresponding quad tree:
#
#
#
# It can be divided according to the definition above:
#
#
#
#  
#
# The corresponding quad tree should be as following, where each node is represented as a (isLeaf, val) pair.
#
# For the non-leaf nodes, val can be arbitrary, so it is represented as *.
#
#
#
# Note:
#
#
# 	N is less than 1000 and guaranteened to be a power of 2.
# 	If you want to know more about the quad tree, you can refer to its wiki.
#
#


"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        leaf = self.is_leaf(grid)
        _len = len(grid)
        if leaf == True:
            node = Node(True, True, None, None, None, None)
        elif leaf == False:
            node = Node(False, True, None, None, None, None)
        else:
            mid = _len // 2
            topLeftGrid = [[grid[i][j] for j in range(mid)] for i in range(mid)]
            topRightGrid = [[grid[i][j] for j in range(mid, _len)] for i in range(mid)]
            bottomLeftGrid = [[grid[i][j] for j in range(mid)] for i in range(mid, _len)]
            bottomRightGrid = [[grid[i][j] for j in range(mid, _len)] for i in range(mid, _len)]
            node = Node(True, False, self.construct(topLeftGrid), self.construct(topRightGrid), 
                        self.construct(bottomLeftGrid), self.construct(bottomRightGrid))
        return node
        
        
        
    def is_leaf(self, grid):
        N = len(grid)
        s = set()
        for i in range(N):
            for j in range(N):
                s.add(grid[i][j])
        if len(s) == 1:
            if grid[0][0] == 1:
                return True
            else:
                return False
        else:
            return None
