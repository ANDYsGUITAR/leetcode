# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
#
#


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # ans = []
        # for i in range(1, len(nums) + 1):
        #     if i not in nums:
        #         ans.append(i)
        # return ans
        
        
        # if nums  == []:
        #     return []
        # ans = []
        # s = sorted(nums)
        # mini = s[0]
        # maxi = s[-1]
        # s = set(s)
        # for i in range(1, len(nums) + 1):
        #     if i < mini:
        #         ans.append(i)
        #     elif i > maxi:
        #         ans.append(i)
        #     else:
        #         if i not in s:
        #             ans.append(i)
        # return ans
        
        
        return list(set(range(1, len(nums) + 1)) - set(nums))
