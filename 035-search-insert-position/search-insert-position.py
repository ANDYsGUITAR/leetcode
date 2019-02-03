# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
#
# You may assume no duplicates in the array.
#
# Example 1:
#
#
# Input: [1,3,5,6], 5
# Output: 2
#
#
# Example 2:
#
#
# Input: [1,3,5,6], 2
# Output: 1
#
#
# Example 3:
#
#
# Input: [1,3,5,6], 7
# Output: 4
#
#
# Example 4:
#
#
# Input: [1,3,5,6], 0
# Output: 0
#
#


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
            return 0
        if nums[0] >= target:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        if nums[-1] < target:
            return len(nums)
        left = nums[0]
        for i in range(0, len(nums) - 1):
            if nums[i] == target:
                return i
            elif nums[i] < target < nums[i + 1]:
                return i + 1
