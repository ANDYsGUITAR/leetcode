# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
#
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).
#
#  
#
# Example 1:
#
#
# Input: [[4,3,8,4],
#         [9,5,1,9],
#         [2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
#
# while this one is not:
# 384
# 519
# 762
#
# In total, there is only one magic square inside the given grid.
#
#
# Note:
#
#
# 	1 <= grid.length <= 10
# 	1 <= grid[0].length <= 10
# 	0 <= grid[i][j] <= 15
#
#


class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
#         self.count = 0
#         def is_magic(grid):
#             s = set()
#             for i in range(0,3):
#                 for j in range(0,3):
#                     if grid[i][j] not in range(1,10):
#                         return False
#                     s.add(grid[i][j])
#             if len(s) == 1:
#                 return False
#             total = sum(grid[0])
#             for i in (1,2):
#                 if sum(grid[i]) != total:
#                     return False
#             for j in range(0,3):
#                 tmp = 0
#                 for i in range(0, 3):
#                     tmp += grid[i][j]
#                 if tmp != total:
#                     return False
#             tmp = 0
#             for i in range(0,3):
#                 tmp += grid[i][i]
#             if tmp != total:
#                 return False
#             tmp = 0
#             for i in range(0,3):
#                 tmp += grid[i][2-i]
#             if tmp != total:
#                 return False
#             self.count += 1
            
#         m = len(grid)
#         n = len(grid[0])
#         if m < 3 or n < 3:
#             return 0
        
#         for i in range(m - 3 + 1):
#             for j in range(n - 3 + 1):
#                 curr = [[c for c in grid[i+x][j:j+3]] for x in range(3)]
#                 is_magic(curr)
#         return self.count
        
        
        def is_magic(i, j):
            if grid[i][j] % 2 == 1 or grid[i+1][j+1] != 5:
                return 0
            l = [grid[i][j], grid[i][j+1], grid[i][j+2], grid[i+1][j+2], grid[i+2][j+2], grid[i+2][j+1], grid[i+2][j], grid[i+1][j]]
            s = ''.join([str(x) for x in l])
            if s in '43816729' *2 or s in '43816729'[::-1] * 2:
                return 1
            else:
                return 0
        ans = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                ans += is_magic(i, j)
        return ans
                
        
        
        
        
    
