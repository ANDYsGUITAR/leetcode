# -*- coding:utf-8 -*-


# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
#              return 964176192 represented in binary as 00111001011110000010100101000000.
#
#
# Follow up:
# If this function is called many times, how would you optimize it?


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        s = r'^(0b)(.*)'
        b_str = bin(n)
        m = re.match(s,b_str)
        zero_one = m.group(2)
        length = len(zero_one)
        zero_one = '0'*(32-length)+zero_one
        reverse = zero_one[::-1]
        result = int(reverse,2)
        return result
        
