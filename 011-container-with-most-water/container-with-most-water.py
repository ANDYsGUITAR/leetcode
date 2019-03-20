# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
# Note: You may not slant the container and n is at least 2.
#
#  
#
#
#
# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49. 
#
#  
#
# Example:
#
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
#


class Solution:
    def maxArea(self, height: 'List[int]') -> 'int':
        # tle
        
        # def helper(height, i, j):
        #     return (j - i) * min(height[i], height[j])
        # ans = 0
        # for i in range(len(height) - 1):
        #     for j in range(i + 1, len(height)):
        #         tmp = helper(height, i, j)
        #         ans = max(ans, tmp)
        # return ans
        
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            ans = max(ans, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans 
