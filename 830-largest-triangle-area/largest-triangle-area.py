# You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.
#
#
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the largest.
#
#
#
#
# Notes: 
#
#
# 	3 <= points.length <= 50.
# 	No points will be duplicated.
# 	 -50 <= points[i][j] <= 50.
# 	Answers within 10^-6 of the true value will be accepted as correct.
#
#
#  
#


class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        N = len(points)
        ans = 0
        for p1, p2, p3 in itertools.combinations(points, 3):
            ans = max(ans, self.calc(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1]))
        return ans
    def calc(self, x1, y1, x2, y2, x3, y3):
            return 0.5 * abs((x2 - x1)*(y3 - y1) - (x3 - x1)*(y2 - y1))
