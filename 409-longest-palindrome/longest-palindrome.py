# Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
#
# This is case sensitive, for example "Aa" is not considered a palindrome here.
#
# Note:
# Assume the length of given string will not exceed 1,010.
#
#
# Example: 
#
# Input:
# "abccccdd"
#
# Output:
# 7
#
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
#
#


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        ans = 0
        odd = False
        for v in count.values():
            if v % 2 != 0:
                odd = True
                if v > 2:
                    ans += v - 1
            else:
                ans += v
        if odd:
            ans += 1
        return ans
        
        
