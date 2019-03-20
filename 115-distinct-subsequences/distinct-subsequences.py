# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
#   ^  ^^
# babgbag
#     ^^^
#
#


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
        for i in range(len(s) + 1):
            for j in range(len(t) + 1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0 and j != 0:
                    pass
                elif i != 0 and j == 0:
                    dp[i][j] = 1
                else:
                    if s[i- 1] == t[j - 1]:
                        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i - 1][j]
        return dp[len(s)][len(t)]
                    
