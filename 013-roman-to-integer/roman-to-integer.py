# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
#
#
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
#
#
# 	I can be placed before V (5) and X (10) to make 4 and 9. 
# 	X can be placed before L (50) and C (100) to make 40 and 90. 
# 	C can be placed before D (500) and M (1000) to make 400 and 900.
#
#
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
#
# Example 1:
#
#
# Input: "III"
# Output: 3
#
# Example 2:
#
#
# Input: "IV"
# Output: 4
#
# Example 3:
#
#
# Input: "IX"
# Output: 9
#
# Example 4:
#
#
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#
#
# Example 5:
#
#
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        result = 0
        n = len(s)
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(n-1,-1,-1):
            if i == n-1:
                result += d[s[i]]
            elif d[s[i]]<d[s[i+1]]:
                result -= d[s[i]]
            else:
                result += d[s[i]]
        return result
                
                
    # def sumRoman(self,s,sum_now):
    #     n = len(s)
    #     if s[0] == 'I':
    #         if n == 1:
    #             sum_now = sum_now + 1
    #         elif s[1] == 'V' and n != 2:
    #             sum_now = sum_now + 4
    #             return self.sumRoman(s[2:],sum_now)
    #         elif s[1] == 'V' and n == 2:
    #             sum_now = sum_now + 4
    #         elif s[1] == 'X' and n!= 2:
    #             sum_now = sum_now + 9
    #             return self.sumRoman(s[2:],sum_now)
    #         elif s[1] == 'X' and n == 2:
    #             sum_now = sum_now + 9
    #         else:
    #             sum_now = sum_now + 1
    #             return self.sumRoman(s[1:],sum_now)
    #     if s[0] == 'X':
    #         if n == 1:
    #             sum_now = sum_now + 10
    #         elif s[1] == 'L' and n != 2:
    #             sum_now = sum_now + 40
    #             return self.sumRoman(s[2:],sum_now)
    #         elif s[1] == 'L' and n == 2:
    #             sum_now = sum_now + 40
    #         elif s[1] == 'C' and n != 2:
    #             sum_now = sum_now + 90
    #             return self.sumRoman(s[2:],sum_now)
    #         elif s[1] == 'C' and n == 2:
    #             sum_now = sum_now + 90
    #         else:
    #             sum_now = sum_now + 10
    #             return self.sumRoman(s[1:],sum_now)
    #     if s[0] == 'C':
    #         if n == 1:
    #             sum_now = sum_now + 100
    #         elif s[1] == 'D' and n != 2:
    #             sum_now = sum_now + 400
    #             return self.sumRoman(s[2:],sum_now)
    #         elif s[1] == 'D' and n == 2:
    #             sum_now = sum_now + 400
    #         elif s[1] == 'M' and n == 2:
    #             sum_now = sum_now + 900
    #         elif s[1] == 'M' and n != 2:
    #             sum_now = sum_now + 900
    #             return self.sumRoman(s[2:],sum_now)
    #         else:
    #             sum_now = sum_now + 100
    #             return self.sumRoman(s[1:],sum_now)
    #     if s[0] == 'V':
    #         if n == 1:
    #             sum_now = sum_now + 5
    #         else:
    #             sum_now = sum_now + 5
    #             return self.sumRoman(s[1:],sum_now)
    #     if s[0] == 'L':
    #         if n == 1:
    #             sum_now = sum_now + 50
    #         else:
    #             sum_now = sum_now + 50
    #             return self.sumRoman(s[1:],sum_now)
    #     if s[0] == 'D':
    #         if n == 1:
    #             sum_now = sum_now + 500
    #         else:
    #             sum_now = sum_now + 500
    #             return self.sumRoman(s[1:],sum_now)
    #     if s[0] == 'M':
    #         if n == 1:
    #             sum_now = sum_now + 1000
    #         else:
    #             sum_now = sum_now + 1000
    #             return self.sumRoman(s[1:],sum_now)
    #     return sum_now
                
