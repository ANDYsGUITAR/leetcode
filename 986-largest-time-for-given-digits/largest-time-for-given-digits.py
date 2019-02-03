# Given an array of 4 digits, return the largest 24 hour time that can be made.
#
# The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.
#
# Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
#
#  
#
#
# Example 1:
#
#
# Input: [1,2,3,4]
# Output: "23:41"
#
#
#
# Example 2:
#
#
# Input: [5,5,5,5]
# Output: ""
#
#
#  
#
# Note:
#
#
# 	A.length == 4
# 	0 <= A[i] <= 9
#
#
#


class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        ans = -1
        for h1, h2, m1, m2 in itertools.permutations(A):
            h = 10 * h1 + h2
            m = 10 * m1 + m2
            time = 60 * h + m
            if 0 <= h < 24 and 0 <= m < 60 and time > ans:
                ans = time
        h = ans // 60
        m = ans - 60 * h
        "{:02}:{:02}".format(h, m)
        return "{:02}:{:02}".format(h, m) if ans >= 0 else ''
