# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#


class Solution:
    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        n = len(nums)
        if n == 0:
            return [[]]
        visited = [0] * n
        ans = []
        nums.sort()
        def dfs(path):
            if len(path) == n:
                ans.append(path)
            else:
                for i in range(n):
                    if not visited[i]:
                        if i > 0  and nums[i] == nums[i - 1] and visited[i - 1] == 0:
                            continue
                        visited[i] = 1
                        dfs(path + [nums[i]])
                        visited[i] = 0
        dfs([])
        return ans
