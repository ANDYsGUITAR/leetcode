# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
# Note:  
#
#
# 	1 is typically treated as an ugly number.
# 	n does not exceed 1690.
#


class Solution:
    ugly = sorted( 2 ** a * 3 ** b * 5 ** c for a in range(32) for b in range(20) for c in range(14))
    def nthUglyNumber(self, n: int) -> int:
        # dp = [1]
        # t2 = t3 = t5 = 0
        # while len(dp) < n:
        #     while dp[t2] * 2 <= dp[-1]:
        #         t2 += 1
        #     while dp[t3] * 3 <= dp[-1]:
        #         t3 += 1
        #     while dp[t5] * 5<= dp[-1]:
        #         t5 += 1
        #     dp.append(min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5))
        # return dp[-1]
        return self.ugly[n - 1]
