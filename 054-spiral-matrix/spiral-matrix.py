# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
#
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix is None or len(matrix) == 0:
            return []
        result = []
        visited = []
        self.helper(matrix, 0, 0, 'right', result,visited)
        return result
    
    def helper(self, matrix, i, j, direction, result, visited):
        coor = [i,j]
        if coor in visited:
            return
        else:
            visited.append(coor)
        n = len(matrix)
        m = len(matrix[0])
        if i < 0 or j < 0 or i > n-1 or j > m -1:
            return
        result.append(matrix[i][j])
        if j == m - i - 1 and direction == 'right' and i < n - 1:
            self.helper(matrix, i+1, j, 'down', result,visited)
        elif j == m - n + i and direction == 'down':
            self.helper(matrix, i, j - 1, 'left', result,visited)
        elif i == n - 1 - j and direction == 'left':
            self.helper(matrix, i-1, j, 'up', result,visited)
        elif i == j + 1 and direction == 'up':
            self.helper(matrix, i, j+1, 'right', result,visited)
        else:
            if direction == 'up':
                self.helper(matrix, i-1, j, 'up', result,visited)
            elif direction == 'down':
                self.helper(matrix, i+1, j, 'down', result,visited)
            elif direction == 'left':
                self.helper(matrix, i, j-1, 'left', result,visited)
            else:
                self.helper(matrix, i, j+1, 'right', result,visited)
