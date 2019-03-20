# The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
#
#
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
#
# Example:
#
#
# Input: 4
# Output: [
#  [".Q..",  // Solution 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // Solution 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
#
#


class Solution:
    def solveNQueens(self, n: 'int') -> 'List[List[str]]':
        def DFS(queens, xy_dif, xy_sum):
                p = len(queens)
                if p==n:
                    result.append(queens)
                    return None
                for q in range(n):
                    if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                        DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])  
        result = []
        DFS([],[],[])
        print(result)
        return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
            
            
            
            
            
        # haven't done yet
#         def miss(board, curr):
#             if curr >= n:
#                 return (-1, -1)
#             else:
#                 for i in range(n):
#                     for j in range(n):
#                         if board[i][j] == '.':
#                             return (i, j)
        
#         def checkRow(board, row, col):
#             for j in range(n):
#                 if j != col and board[row][j] == 'Q':
#                     return False
#             return True
        
#         def checkCol(board, row, col):
#             for i in range(n):
#                 if i != row and board[i][col] == 'Q':
#                     return False
#             return True
        
#         def checkDiag(board, row, col):
#             for i in range(n):
#                 j = col - row + i
#                 if i != row and j != col and board[i][j] == 'Q':
#                     return False
#                 j = row + col - i
#                 if i != row and j != col and board[i][j] == 'Q':
#                     return False
#             return True
        
#         def isSafe(board, row, col):
#             return checkRow(board, row, col) and checkCol(board, col, row) and checkDiag(board, row, col)
        
#         def solve(board, curr, ans):
#             row, col = miss(board, curr)
#             if row == col == -1:
#                 ans.append(board)
#                 return True
#             if isSafe(board, row, col):
#                 board[row][col] = 'Q'
#                 if solve(board, curr + 1, ans):
#                     return True
#                 else:
#                     board[row][col] = '.'
                
#         board = [['.' for i in range(n)] for j in range(n)]
#         print(board)
#         ans = []
#         solve(board, 0, ans)
#         return ans

        
            
                    

