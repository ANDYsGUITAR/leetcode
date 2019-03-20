# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#


class Solution:
    def longestPalindrome(self, s):
        
        # def helper(s):
        #     return s == s[::-1]
        # n = len(s)
        # if n <= 1:
        #     return s
        # l = 0
        # ans = ''
        # for i in range(n-1):
        #     for j in range(i+1, n+1):
        #         if helper(s[i:j]):
        #             if j - i > l:
        #                 ans = s[i:j]
        #                 l = j - i
        # return ans
         
        def helper(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        n = len(s)
        if n <= 1:
            return s
        ans = ''
        for i in range(n):
            tmp = helper(s, i, i)
            if len(tmp) > len(ans):
                ans = tmp
            tmp = helper(s, i, i+1)
            if len(tmp) > len(ans):
                ans = tmp
        return ans 
