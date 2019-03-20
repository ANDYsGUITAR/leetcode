# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
#
#
# Given input matrix = 
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#
#
# Example 2:
#
#
# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ], 
#
# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
#
#


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
#         if len(matrix) <= 1:
#             pass
#         else:    
#             n = len(matrix)
#             # 一圈一圈旋转 要处理 n // 2 圈
#             count = n // 2
#             for i in range(count):
#                 # 每圈从[i][i] 到 [i][n-i-1]
#                 rotate_round(matrix, i)
        


# def rotate_round(matrix, k):
#     n = len(matrix)
#     for i in range(k, n-k-1):
#         matrix[k][i], matrix[i][n-k-1] = matrix[i][n-k-1], matrix[k][i]
#         matrix[n-k-1][n-1-i], matrix[k][i] = matrix[k][i], matrix[n-k-1][n-1-i]
#         matrix[n - i - 1][k], matrix[k][i] = matrix[k][i], matrix[n - i - 1][k]

#         /*
#  * clockwise rotate
#  * first reverse up to down, then swap the symmetry 
#  * 1 2 3     7 8 9     7 4 1
#  * 4 5 6  => 4 5 6  => 8 5 2
#  * 7 8 9     1 2 3     9 6 3
# */

        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    

