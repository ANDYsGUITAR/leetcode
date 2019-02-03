#
# Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
#
#
# Example:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#
#
#
# Restrictions: 
#
#  The string consists of lower English letters only.
#  Length of the given string and k will in the range [1, 10000]
#


class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # if k == 1:
        #     return s
        # if len(s) < k:
        #     return s[::-1]
        # ans = ''
        # n = len(s)
        # a = int(n / 2*k)
        # for i in range(a):
        #     x = s[i*2*k : i*2*k+k]
        #     x = x[::-1]
        #     ans += x + s[i*2*k+k : (i+1)*2*k]
        # if n - 2*k*a != 0:
        #     if n - 2*k*a < k:
        #         ans += s[(a-1)*2*k:][::-1]
        #     else:
        #         ans += s[(a-1)*2*k : (a-1)*2*k + k][::1]
        #         ans += s[(a-1)*2*k + k:]
        # return ans
        
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return ''.join(a)
            
            
        
        
