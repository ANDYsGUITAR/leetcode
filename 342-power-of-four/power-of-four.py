# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example 1:
#
#
# Input: 16
# Output: true
#
#
#
# Example 2:
#
#
# Input: 5
# Output: false
#
#
# Follow up: Could you solve it without loops/recursion?


class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        if num == 1:
            return True
        b = "{0:b}".format(num)
        if b[0] == '1' and b.count('0') % 2 == 0 and b.count('1') == 1:
            return True
        return False
