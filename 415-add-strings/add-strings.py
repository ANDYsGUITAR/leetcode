# -*- coding:utf-8 -*-


# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ans = ''
        while i >= 0 or j >= 0:
            if i >= 0:
                carry += ord(num1[i]) - ord('0')
            if j >= 0:
                carry += ord(num2[j]) - ord('0')
            ans += chr(carry % 10 + ord('0'))
            carry //= 10
            i -= 1
            j -= 1
        if carry == 1:
            ans += '1'
        return ans[::-1]
