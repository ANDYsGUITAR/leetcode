# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
#
# Note:
#
#
# 	Both dividend and divisor will be 32-bit signed integers.
# 	The divisor will never be 0.
# 	Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
#
#


class Solution:
    def divide(self, a: 'int', b: 'int') -> 'int':
        sign = (a < 0) == (b < 0)
        a, b, ans = abs(a), abs(b), 0
        while a >= b:
            tmp = b
            i = 1
            while a >= tmp:
                a -= tmp
                ans += i
                tmp <<= 1
                i <<= 1
        if not sign:
            ans = - ans
        return min(ans, 2147483647)
