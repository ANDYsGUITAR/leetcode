# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
#
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# Note: m and n will be at most 100.
#
# Example 1:
#
#
# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: 'List[List[int]]') -> 'int':
        # in place dp
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        for i in range(1, n):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, m):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, m):
            for j in range(1, n):
                obstacleGrid[i][j] = (obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]
