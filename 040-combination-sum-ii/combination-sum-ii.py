# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
#
# Each number in candidates may only be used once in the combination.
#
# Note:
#
#
# 	All numbers (including target) will be positive integers.
# 	The solution set must not contain duplicate combinations.
#
#
# Example 1:
#
#
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#
# Example 2:
#
#
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
#
#


class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        ans = []
        def backTrack(curr, need, start):
            if need == 0:
                ans.append(curr)
                return
            for i in range(start, len(candidates)):
                if candidates[i] > need:
                    break
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                else:
                    backTrack(curr + [candidates[i]], need - candidates[i], i + 1)
                
        if len(candidates) == 0 or target == 0:
            return ans
        backTrack([], target, 0)
        return ans
