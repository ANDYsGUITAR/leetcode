# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
#
# Example 1:
#
#
# Input: num1 = "2", num2 = "3"
# Output: "6"
#
# Example 2:
#
#
# Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
# Note:
#
#
# 	The length of both num1 and num2 is < 110.
# 	Both num1 and num2 contain only digits 0-9.
# 	Both num1 and num2 do not contain any leading zero, except the number 0 itself.
# 	You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


class Solution:
    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        m , n = len(num1), len(num2)
        result = [0] * (m + n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                pos1 = i + j + 1
                pos2 = i + j
                mul += result[pos1]
                result[pos1] = mul % 10
                result[pos2] += mul // 10
        ans = []
        for res in result:
            if len(ans) != 0 or res != 0:
                ans.append(res)
        return ''.join(str(s) for s in ans) if len(ans) != 0 else '0'
