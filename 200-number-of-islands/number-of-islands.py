# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        n = len(grid)
        m = len(grid[0])
        result = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.DFSisland(grid,i,j)
                    result += 1
        return result
                
    def DFSisland(self,grid,i,j):
        if i < 0 or j<0 or i>=len(grid) or j>=len(grid[0]):
            return
        if grid[i][j] == '1':
            grid[i][j] = 0
            self.DFSisland(grid,i+1,j)
            self.DFSisland(grid,i-1,j)
            self.DFSisland(grid,i,j+1)
            self.DFSisland(grid,i,j-1)
        
        
