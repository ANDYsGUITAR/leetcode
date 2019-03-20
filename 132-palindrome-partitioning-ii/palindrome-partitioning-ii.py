# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
#


class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        cut = [x for x in range(-1, len(s))]
        for i in range(len(s)):
            r1, r2 = 0, 0
            while i - r1 >= 0 and i + r1 < len(s) and s[i - r1] == s[i + r1]:
                cut[i + r1 + 1] = min(cut[i + r1 + 1], cut[i - r1] + 1)
                r1 += 1
            while i - r2 >= 0 and i + r2 + 1 < len(s) and s[i - r2] == s[i + r2 + 1]:
                cut[i + r2 + 2] = min(cut[i + r2 + 2], cut[i - r2] + 1)
                r2 += 1
        return cut[-1]
        
        
        # MLE
#         def isP(s):
#             return s == s[::-1]
        
#         def dfs(s, path, res):
#             if not s:
#                 res.append(path)
#             else:
#                 for i in range(1, len(s) + 1):
#                     if isP(s[:i]):
#                         dfs(s[i:], path + [s[:i]], res)
                        
#         res = []
#         dfs(s, [], res)
#         ans = float('inf')
#         for p in res:
#             ans = min(len(p), ans)
#         return ans - 1

        
