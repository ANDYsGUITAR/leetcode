# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#


import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        if n <= 2:
            return 0
        prime = [1]*n
        prime[0] = 0
        prime[1] = 0
        for i in range(2, n):
            if prime[i] == 1:
                prime[i*i:n:i] = [0]*len(prime[i*i:n:i])
        return sum(prime)

