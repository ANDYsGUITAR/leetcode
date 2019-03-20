# The set [1,2,3,...,n] contains a total of n! unique permutations.
#
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
#
#
# 	"123"
# 	"132"
# 	"213"
# 	"231"
# 	"312"
# 	"321"
#
#
# Given n and k, return the kth permutation sequence.
#
# Note:
#
#
# 	Given n will be between 1 and 9 inclusive.
# 	Given k will be between 1 and n! inclusive.
#
#
# Example 1:
#
#
# Input: n = 3, k = 3
# Output: "213"
#
#
# Example 2:
#
#
# Input: n = 4, k = 9
# Output: "2314"
#
#


class Solution:
    def getPermutation(self, n: 'int', k: 'int') -> 'str':
        # too slow
        # from itertools import permutations
        # p = permutations(range(1, n+1))
        # p = list(p)
        # result = p[k - 1]
        # return ''.join(str(s) for s in result)
        
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n - 1)
        if n == 1:
            return '1'
        nums = [i for i in range(1, n + 1)]
        ans = ''
        curr = n
        f = factorial(n-1)
        while len(nums) != 1:
            idx = k // f if k % f != 0 else k // f - 1
            num = nums[idx]
            ans = ans + str(num)
            nums.remove(num)
            k = k - idx * f
            f //= curr - 1
            curr -= 1
            if k == 1:
                ans = ans + ''.join(str(c) for c in nums)
                break
        return ans
            
