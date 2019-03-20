# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Determine if you are able to reach the last index.
#
# Example 1:
#
#
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
#
# Example 2:
#
#
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum
#              jump length is 0, which makes it impossible to reach the last index.
#
#


class Solution:
    def canJump(self, nums: 'List[int]') -> 'bool':
        n = len(nums)
        if n == 0:
            return False
        if n == 1:
            return True
        max_position = 0
        end = 0
        for i in range(n - 1):
            max_position = max(max_position, nums[i] + i)
            if i == end:
                end = max_position
        print(end)
        return end >= n - 1
