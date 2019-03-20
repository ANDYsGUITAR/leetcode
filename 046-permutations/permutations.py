# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        # method 1
        # import itertools
        # return list(itertools.permutations(nums))
        
        
        # method 2
        # def dfs(nums, path, result):
        #     if len(nums) == 0:
        #         result.append(path)
        #     else:
        #         for i in range(len(nums)):
        #             dfs(nums[:i] + nums[i+1:], path+[nums[i]], result)
        # result = []
        # dfs(nums, [], result)
        # return result
        
        # method 3
        
        ans = []
        visited = [0] * len(nums)
        def dfs(path):
            if len(path) == len(nums):
                ans.append(path)
            else:
                for i in range(len(nums)):
                    if not visited[i]:
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        dfs([])
        return ans
            
                
        
