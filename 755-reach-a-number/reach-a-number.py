#
# You are standing at position 0 on an infinite number line.  There is a goal at position target.
#
# On each move, you can either go left or right.  During the n-th move (starting from 1), you take n steps.
#
# Return the minimum number of steps required to reach the destination.
#
#
# Example 1:
#
# Input: target = 3
# Output: 2
# Explanation:
# On the first move we step from 0 to 1.
# On the second step we step from 1 to 3.
#
#
#
# Example 2:
#
# Input: target = 2
# Output: 3
# Explanation:
# On the first move we step from 0 to 1.
# On the second move we step  from 1 to -1.
# On the third move we step from -1 to 2.
#
#
#
# Note:
# target will be a non-zero integer in the range [-10^9, 10^9].
#


class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        n = (-1 +(1 + 8 * target) ** 0.5) / 2
        if n - int(n) == 0:
            return int(n)
        m = int(n) + 1
        curr = (m**2 + m) / 2
        exceed = curr - target
        if exceed % 2 == 0:
            return m
        elif (exceed + m + 1) % 2 == 0:
            return m + 1
        else:
            return m + 2
