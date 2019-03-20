# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# Example 1:
#
#
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
#
#
# Example 2:
#
#
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
#


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        dp1 = [x for x in nums] # +
        dp2 = [x for x in nums] # -
        for i in range(1, n):
            if nums[i] > 0:
                if dp1[i - 1] > 0:
                    dp1[i] *= dp1[i - 1]
                if dp2[i - 1] < 0:
                    dp2[i] *= dp2[i - 1]
            elif nums[i] < 0:
                if dp2[i - 1] < 0:
                    dp1[i] *= dp2[i - 1]
                if dp1[i - 1] > 0:
                    dp2[i] *= dp1[i - 1]
        print(dp1)
        print(dp2)
        return max(max(dp1), max(dp2))

        
        
