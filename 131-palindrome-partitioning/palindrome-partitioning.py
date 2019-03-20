# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# Example:
#
#
# Input: "aab"
# Output:
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
#
#


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isP(s):
            return s == s[::-1]
        
        def dfs(s, path, res):
            if not s:
                res.append(path)
            else:
                for i in range(1, len(s) + 1):
                    if isP(s[:i]):
                        dfs(s[i:], path + [s[:i]], res)
                        
        res = []
        dfs(s, [], res)
        return res
