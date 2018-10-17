# -*- coding:utf-8 -*-


#
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.  
#
#
# Example 1:
#
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
#
#
#
# Note:
#
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
#
#


class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        dp = collections.Counter()
        dp[0] = 1
        for n in nums:
            ndp = collections.Counter()
            for sign in (-1,1):
                for k in dp.keys():
                    ndp[k+sign*n] += dp[k]
            dp = ndp
        return dp[S]
#         if nums is None or len(nums)==0:
#             return 0
#         return self.helper(nums,0,0,S)
        
        
#     def helper(self, nums,index,now,S):
#         if index == len(nums):
#             if now == S:
#                 return 1
#             else:
#                 return 0
#         return self.helper(nums,index+1,now-nums[index],S)+self.helper(nums,index+1,now+nums[index],S)
        
    
    
