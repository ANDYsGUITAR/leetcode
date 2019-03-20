# Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
# Example:
#
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#
#


class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        diff = float('inf')
        nums.sort()
        ans = 0
        n = len(nums)
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(target - s) < diff:
                    diff = abs(target - s)
                    ans = s
                if s < target:
                    l += 1
                elif s == target:
                    return target
                else:
                    r -= 1
        return ans
                    
