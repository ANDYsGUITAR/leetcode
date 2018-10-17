# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
#  
#
# Example:
#
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]
#
# Explanation:
#
#
#
#  
#
# Note:
#
# The total number of elements of the given matrix will not exceed 10,000.
#


class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if matrix == []:
            return []
        self.helper(matrix,0,0,result,'positive')
        return result
        
    def helper(self,matrix,i,j,result,direction):
        result.append(matrix[i][j])
        if i == len(matrix)-1 and j == len(matrix[0])-1:
            return
        elif i == 0 and j < len(matrix[0])-1 and direction == 'positive':
            self.helper(matrix,i,j+1,result,'negative')
        elif i == len(matrix)-1 and j < len(matrix[0])-1 and direction == 'negative':
            self.helper(matrix,i,j+1,result,'positive')
        elif j == 0 and i < len(matrix)-1 and direction == 'negative':
            self.helper(matrix,i+1,j,result,'positive')
        elif j == len(matrix[0])-1 and i < len(matrix)-1 and direction == 'positive':
            self.helper(matrix,i+1,j,result,'negative')
        
        else:
            if direction == 'positive':
                self.helper(matrix,i-1,j+1,result,'positive')
            else:
                self.helper(matrix,i+1,j-1,result,'negative')
            
