# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        import functools
        def cmp(a,b):
            if int(a + b) > int(b + a):
                return 1
            elif int(a + b) < int(b + a):
                return -1
            else:
                return 0
        nums = list(map(str, nums))
        nums.sort(key = functools.cmp_to_key(cmp), reverse = True)
        return ''.join(nums) if nums[0] != '0' else '0'
