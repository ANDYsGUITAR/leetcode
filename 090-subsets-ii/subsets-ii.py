# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
#
#


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, index, path):
            ans.append(path)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                dfs(nums, i + 1, path + [nums[i]])
                    
        ans = []
        nums.sort()
        dfs(nums, 0, [])
        return ans
        
