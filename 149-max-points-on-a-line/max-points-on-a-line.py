# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points: List[Point]) -> int:
        # if not points:
        #     return 0
        # if len(points) == 1:
        #     return 1
        # dic = {}
        # for i in range(len(points)):
        #     for j in range(i + 1, len(points)):
        #         if not (points[i].x == points[j].x and points[i].y == points[j].y):
        #             dic[(points[i].x, points[i].y, points[j].x, points[j].y)] = 0
        # for point in points:
        #     for tur in dic.keys():
        #         x1,y1,x2,y2 = tur
        #         x = point.x
        #         y = point.y
        #         if (x == x1 and y == y1) or (x == x2 and y == y2):
        #             dic[tur] += 1
        #         elif y != y1 and y != y2 and (x - x1) / (y - y1) == (x - x2) / (y - y2):
        #             dic[tur] += 1
        #         elif x == x1 == x2 or y == y1 == y2:
        #             dic[tur] += 1
        #         else:
        #             pass
        # return max(dic.values())
        
        N = len(points)
        res = 0
        for i in range(N):
            lines = collections.defaultdict(int)
            duplicates = 1
            for j in range(i + 1, N):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    duplicates += 1
                    continue
                dx = points[i].x - points[j].x
                dy = points[i].y - points[j].y
                delta = self.gcd(dx, dy)
                lines[(dx / delta, dy / delta)] += 1
            res = max(res, (max(lines.values()) if lines else 0) + duplicates)
        return res
                
    def gcd(self, x, y):
        return x if y == 0 else self.gcd(y, x % y)


