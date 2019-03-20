# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # n = len(nums)
        # result = nums[0]^0
        # for i in range(1,n):
        #     result = result^nums[i]^i
        # return result^n
        n = len(nums)
        result = 0
        for num in nums:
            result ^= num
        for i in range(n + 1):
            result ^= i
        return result
