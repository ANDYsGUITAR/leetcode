# -*- coding:utf-8 -*-


# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#


class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ''
        neg = False
        if num < 0:
            num = -num
            neg = True
        while int(num / 7) != 0:
            ans += str(num % 7)
            num = int(num / 7)
        ans += str(num % 7)
        ans = ans[::-1]
        if neg:
            return '-' + ans
        return ans
        
        
