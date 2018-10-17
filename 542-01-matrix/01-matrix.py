#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1: 
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#
# Example 2: 
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#


class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        result = []
        visited = []
        for i in range(n):
            result.append([0]*m)
        for i in range(n):
            for j in range(m):
                self.Help_updateMatrix(matrix,i,j,result)
        return result
    
    def Help_updateMatrix(self,matrix,i,j,result):
        if matrix[i][j] == 0:
            return
        coordinate = [i,j]
        step = 0
        queue = [coordinate]
        while queue:
            tmp = []
            for q in queue:
                if matrix[q[0]][q[1]] == 0:
                    result[i][j] = step
                    return
                for nq in self.nextCoor(matrix,q):
                    tmp.append(nq)
            queue = tmp
            step += 1
        
    def nextCoor(self,matrix,coordinate):
        i = coordinate[0]
        j = coordinate[1]
        result = []
        if i > 0:
            result.append([i-1,j])
        if i < len(matrix)-1:
            result.append([i+1,j])
        if j > 0:
            result.append([i,j-1])
        if j < len(matrix[0])-1:
            result.append([i,j+1])
        return result
        
        
        
        

                    
                    
            
        
        
