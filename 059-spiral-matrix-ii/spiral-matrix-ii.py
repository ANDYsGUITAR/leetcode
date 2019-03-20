# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
#
# Input: 3
# Output:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#
#


class Solution:
    def generateMatrix(self, n: 'int') -> 'List[List[int]]':
        ans = [[0 for _ in range(n)] for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        curr = 1
        while curr != n * n + 1:
            ans[i][j] = curr
            if ans[(i + di) % n][(j + dj) % n]:
                di, dj = dj, -di
            i += di
            j += dj
            curr += 1
        return ans
