# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
#


class Solution:
    def numDecodings(self, s: str) -> int:
        # dp
        '''
        prev: the ways of prev part
        curr: the ways of curr part
        p: the previous digit
        d: current digit
        '''
        prev, curr, p = 0, int(s > ''), ''
        for d in s:
            prev, curr, p = curr, curr * (d > '0') + prev * (9 < int(p + d) < 27), d
        return curr
