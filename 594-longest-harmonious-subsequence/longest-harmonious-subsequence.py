# -*- coding:utf-8 -*-


# We define a harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1.
#
# Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.
#
# Example 1:
#
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
#
#
#
# Note:
# The length of the input array will not exceed 20,000.
#
#
#


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums, reverse=False)
        l = sorted(set(nums))
        d = {}
        ans = 0
        n = len(nums)
        for i in range(1, len(l)):
            if l[i] - l[i - 1] == 1:
                d[l[i - 1]] = l[i]
        for k, v in d.items():
            start = nums.index(k)
            end = n - nums[::-1].index(v) - 1
            ans = max(ans, end - start + 1)
        return ans
