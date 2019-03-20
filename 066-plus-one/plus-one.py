# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # numStr = ''
        # for d in digits:
        #     numStr += str(d)
        # sumStr = str(int(numStr)+1)
        # result = []
        # for c in sumStr:
        #     result.append(int(c))
        # return result
        n = len(digits)
        if digits[-1] == 9:
            digits[-1] = 0
            if n == 1:
                return [1,0]
            curr = 1
            i = n-2
            while i>0:
                if digits[i] == 9 and curr == 1:
                    digits[i] = 0
                    curr = 1
                else:
                    digits[i] += curr
                    curr = 0
                i -= 1
            if digits[0] == 9 and curr == 1:
                digits[0] = 0
                digits.insert(0,1)
            else:
                digits[0] += curr
            return digits
        else:
            digits[-1] = digits[-1] + 1
            return digits
        
        
