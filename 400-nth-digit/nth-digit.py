# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 
#
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n < 231).
#
#
# Example 1:
#
# Input:
# 3
#
# Output:
# 3
#
#
#
# Example 2:
#
# Input:
# 11
#
# Output:
# 0
#
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
#
#


class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
     # * 这里是找第n个数字(这里的数和数字有区别，数字可以理解为将所有数拼合成一个字符串后的第n为对应的数字（0-9)）
     # * 这里首先分析一下位数和规律
     # * 个位数：1-9，一共9个,共计9个数字
     # * 2位数：10-99,一共90个，共计180个数字
     # * 3位数：100-999，一共900个，共计2700个数字
     # * 4位数，1000-9999，一共9000个，共计36000个数字
     # * 以此类推，
     # * 这样我们就可以首先定位到是哪个数，再找到其对应的数字
     # * */
        digitType = 1 # 位数
        digitNum = 9
        while n > digitType * digitNum:
            n -= digitType * digitNum
            digitType += 1
            digitNum *= 10
        index_in_group = (n - 1) // digitType
        index_in_num = (n - 1) % digitType
        num = 10 ** (digitType - 1) + index_in_group
        ans = str(num)[index_in_num]
        return int(ans)

        
