# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# The array may contain duplicates.
#
# Example 1:
#
#
# Input: [1,3,5]
# Output: 1
#
# Example 2:
#
#
# Input: [2,2,2,0,1]
# Output: 0
#
# Note:
#
#
# 	This is a follow up problem to Find Minimum in Rotated Sorted Array.
# 	Would allow duplicates affect the run-time complexity? How and why?
#
#


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.helper(nums, 0, len(nums)-1)

        

    def helper(self, nums, left, right):
        # only one or two elements
        if right - left <= 1:
            return min(nums[left], nums[right])
        # sorted
        if nums[left] < nums[right]:
            return nums[left]
        mid = (left + right)//2
        return min(self.helper(nums,left, mid-1),self.helper(nums, mid, right))
        
