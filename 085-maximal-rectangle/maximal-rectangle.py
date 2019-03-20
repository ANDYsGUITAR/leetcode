# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Example:
#
#
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
#
#


class Solution:
    def maximalRectangle(self, matrix: 'List[List[str]]') -> 'int':
        def largestRectangleArea(heights: 'List[int]') -> 'int':
            ans = 0
            stack = [-1]
            heights.append(0)
            for i in range(len(heights)):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    ans = max(ans, h * w)
                stack.append(i)
            return ans
        accumulation = [[int(matrix[i][j]) for j in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if accumulation[i][j]:
                    accumulation[i][j] += accumulation[i - 1][j]
        ans = 0
        for row in accumulation:
            ans = max(ans, largestRectangleArea(row))
        return ans
            
