# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
#
#
# Example 1:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
#
#
#
# Example 2:
#
#
# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
#
#
#  
#
# Note:
#
#
# 	You may assume that all elements in nums are unique.
# 	n will be in the range [1, 10000].
# 	The value of each element in nums will be in the range [-9999, 9999].
#
#


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    #     if target in nums:
    #         return self.helper(nums, 0, len(nums),target)
    #     else:
    #         return -1
    # def helper(self, nums, left, right, target):
    #     mid = (left+right)//2
    #     if nums[mid] == target:
    #         return mid
    #     elif target < nums[mid]:
    #         return self.helper(nums, left, mid, target)
    #     else:
    #         return self.helper(nums, mid, right, target)
        if len(nums) == 0:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # End Condition: left > right
        return -1
