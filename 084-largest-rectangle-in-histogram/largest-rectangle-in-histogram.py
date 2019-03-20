# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
#
#  
#
#
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
#
#  
#
#
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
#  
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#


class Solution:
    def largestRectangleArea(self, heights: 'List[int]') -> 'int':
        # # scan from right and left
        # if not heights:
        #     return 0
        # n = len(heights)
        # left, right = [0] * n, [0] * n
        # right[n - 1] = 1
        # for i in range(n - 2, -1, -1):
        #     if heights[i] > heights[i + 1]:
        #         right[i] = 1
        #     else:
        #         j = i + 1
        #         while j < n and heights[j] >= heights[i]:
        #             j += right[j]
        #         right[i] = j - i
        # left[0] = 1
        # for i in range(1, n):
        #     if heights[i] > heights[i - 1]:
        #         left[i] = 1
        #     else:
        #         j = i - 1
        #         while j >= 0 and heights[j] >= heights[i]:
        #             j -= left[j]
        #         left[i] = i - j
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, heights[i]*(right[i] + left[i] - 1))
        # return ans
        
        # stack
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
