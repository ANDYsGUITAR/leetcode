# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
#
# 	Each of the digits 1-9 must occur exactly once in each row.
# 	Each of the digits 1-9 must occur exactly once in each column.
# 	Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
#
#
# Empty cells are indicated by the character '.'.
#
#
# A sudoku puzzle...
#
#
# ...and its solution numbers marked in red.
#
# Note:
#
#
# 	The given board contain only digits 1-9 and the character '.'.
# 	You may assume that the given Sudoku puzzle will have a single unique solution.
# 	The given board size is always 9x9.
#
#


class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """
        def miss(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        return (row, col)
            return (-1, -1)
        
        def checkRow(board, row, num):
            for col in range(9):
                if board[row][col] == num:
                    return False
            return True
        
        def checkCol(board, col, num):
            for row in range(9):
                if board[row][col] == num:
                    return False
            return True
        
        def checkBox(board, row, col, num):
            for i in range(3):
                for j in range(3):
                    if board[(row // 3) * 3 + i][(col // 3) * 3 + j] == num:
                        return False
            return True
        
        def isSafe(board, row, col, num):
            return checkRow(board, row, num) and checkCol(board, col, num) and checkBox(board, row, col, num)
        
        def solve(board):
            row, col = miss(board)
            if row == col == -1:
                return True
            s = '123456789'
            for num in s:
                if isSafe(board, row, col, num):
                    board[row][col] = num
                    if solve(board):
                        return True
                    board[row][col] = '.'
            return False
        
        solve(board)
