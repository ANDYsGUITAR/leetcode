# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#


class Solution:
    # def __init__(self):
    #     self.ans = float('inf')
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # TLE
        # n = len(triangle)
        # def dfs(i, j, cur):
        #     if i == n - 1:
        #         self.ans = min(self.ans, triangle[i][j] + cur)
        #     else:
        #         dfs(i + 1, j, cur + triangle[i][j])
        #         dfs(i + 1, j + 1, cur + triangle[i][j])
        # dfs(0, 0, 0)
        # return self.ans
        
        dp = triangle
        n = len(dp)
        for i in range(1, n):
            for j in range(len(dp[i])):
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                elif j == len(dp[i]) - 1:
                    dp[i][j] += dp[i - 1][j - 1]
                else:
                    dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j])
        return min(dp[-1])
