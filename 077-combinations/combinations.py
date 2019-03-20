# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#
#


class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        
        # too slow
#         nums = [i for i in range(1, n + 1)]
        
#         def backTrack(curr, remain, need):
#             if need == 0:
#                 ans.append(curr)
#             else:
#                 for i in range(len(remain)):
#                     if not curr or (len(curr) >= 1 and remain[i] > curr[-1]):
#                         backTrack(curr + [remain[i]], remain[:i] + remain[i + 1:], need - 1)
#         ans = []
#         backTrack([], nums, k)
#         return ans

        # provided
        # from itertools import combinations
        # return list(combinations(range(1, n + 1), k))
        
        # recursive
        if k  == 0:
            return[[]]
        return [pre + [i] for i in range(k, n + 1) for pre in self.combine(i - 1, k - 1)]
