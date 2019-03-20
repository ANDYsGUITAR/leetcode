# Given an array of non-negative integers, you are initially positioned at the first index of the array.
#
# Each element in the array represents your maximum jump length at that position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
#     Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#


class Solution:
    def jump(self, nums: 'List[int]') -> 'int':
        # dp TLE O(n^2)
        # n = len(nums)
        # if n <= 1:
        #     return 0
        # if nums[0] > n - 1:
        #     return 1
        # dp = [1 if i + nums[i] >= n - 1 else float('inf') for i in range(n)]
        # dp[-1] = 0
        # if dp[0] == 1:
        #     return 1
        # for i in range(n-2, -1, -1):
        #     tmp = nums[i]
        #     j = i + 1
        #     while j < n and j <= i + tmp:
        #         dp[i] = min(dp[i], 1 + dp[j])
        #         j += 1
        # return dp[0]
        
        # greedy
        # O(n^2)
        # n = len(nums)
        # if n <= 1:
        #     return 0
        # position = n - 1
        # step = 0
        # while position != 0:
        #     for i in range(0, position):
        #         if nums[i] + i >= position:
        #             position = i
        #             step += 1
        #             break
        # return step
        
        # greedy
        # O(n^2)
        
        n = len(nums)
        if n <= 1:
            return 0
        step = 0
        end = 0
        max_position = 0
        for i in range(n - 1):
            max_position = max(max_position, i + nums[i])
            if i == end:
                end = max_position
                step += 1
        return step
                
