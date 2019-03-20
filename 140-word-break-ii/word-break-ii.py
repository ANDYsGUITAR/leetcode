# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
#
# Note:
#
#
# 	The same word in the dictionary may be reused multiple times in the segmentation.
# 	You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
#   "cats and dog",
#   "cat sand dog"
# ]
#
#
# Example 2:
#
#
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
#


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def dfs(s, res, wordDict, memo):
            if s in memo:
                return memo[s]
            if not s:
                return ['']
            res = []
            for word in wordDict:
                if s.startswith(word):
                    l = len(word)
                    for r in dfs(s[l:], res, wordDict, memo):
                        res.append(word + ('' if not r else ' ' + r))
            memo[s] = res
            return res
        res = []
        memo = {}
        return dfs(s, res, wordDict, memo)
#         def dfs(s, path, ans):
#             if not s:
#                 tmp = ' '.join(w for w in path)
#                 ans.append(tmp)
#             else:
#                 for word in wordDict:
#                     if s.startswith(word):
#                         l = len(word)
#                         dfs(s[l:], path + [word], ans)
                        
#         ans = []
#         dfs(s, [], ans)
#         return ans

