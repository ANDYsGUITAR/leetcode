# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
#
#
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!
#
# Example:
#
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
#


class Solution:
    def trap(self, height: 'List[int]') -> 'int':
        # method 1 brute force
        # O(n^2)
        
        # ans = 0
        # for i in range(len(height)):
        #     left_most = right_most = 0
        #     for j in range(0, i + 1):
        #         left_most = max(left_most, height[j])
        #     for j in range(i, len(height)):
        #         right_most = max(right_most, height[j])
        #     ans += min(left_most, right_most) - height[i]
        # return ans
    
        # method 2 optimize method 1
        # O(n)
        
        # ans = 0
        # left_most = {}
        # right_most = {}
        # most = 0
        # for i in range(len(height)):
        #     most = max(most, height[i])
        #     left_most[i] = most
        # most = 0
        # for i in range(len(height) - 1, -1, -1):
        #     most = max(most, height[i])
        #     right_most[i] = most
        # for i in range(len(height)):
        #     ans += min(left_most[i], right_most[i]) - height[i]
        # return ans
        
        # method 3 stack
        # O(n)
        
#         ans = 0
#         curr = 0
#         stack = []
#         while curr < len(height):
#             while len(stack) > 0 and (height[curr] > height[stack[-1]]):
#                 top = stack[-1]
#                 stack.pop()
#                 if len(stack) == 0:
#                     break
#                 distance = curr - stack[-1] - 1
#                 bound = min(height[curr], height[stack[-1]]) - height[top]
#                 ans += distance * bound
#             stack.append(curr)
#             curr += 1
            
#         return ans

        # method 4 two pointers
        # O(n)
        
        left, right = 0, len(height) - 1
        ans = 0
        left_max = right_max = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
                
        return ans
                    
        
                
    
    
