# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
#
#
# Note:
#
#
# 	If there is no such window in S that covers all characters in T, return the empty string "".
# 	If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
#


class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        if not t or not s:
            return ''
        count = collections.Counter(t)
        required = len(count)
        l = r = 0
        curr = 0
        window_count = {}
        ans = (float('inf'), None, None)
        while r < len(s):
            c = s[r]
            window_count[c] = window_count.get(c, 0) + 1
            if c in count and window_count[c] == count[c]:
                curr += 1
            while l <= r and curr == required:
                c = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_count[c] -= 1
                if c in count and window_count[c] < count[c]:
                    curr -= 1
                l += 1
            r += 1
        return '' if ans[0] == float('inf') else s[ans[1] : ans[2] + 1]
