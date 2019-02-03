# Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.
#
# Example:
#
# Input:
# [1,2,3]
#
# Output:
# 3
#
# Explanation:
# Only three moves are needed (remember each move increments two elements):
#
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
#
#


class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # count = 0
        # while len(set(nums)) != 1:
        #     nums = sorted(nums)
        #     nums = [n+1 for n in nums[:len(nums)-1]] + [nums[-1]]
        #     count += 1
        # return count
        
        return sum(nums) - len(nums) * min(nums)
