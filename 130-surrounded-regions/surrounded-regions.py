# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
#
# X X X X
# X O O X
# X X O X
# X O X X
#
#
# After running your function, the board should be:
#
#
# X X X X
# X X X X
# X X X X
# X O X X
#
#
# Explanation:
#
# Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def DFSnot(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if board[i][j] == 'O':
                board[i][j] = '$'
                DFSnot(board, i + 1, j)
                DFSnot(board, i - 1, j)
                DFSnot(board, i, j + 1)
                DFSnot(board, i, j - 1)
        def DFS(board, i, j):
            if i < 0 or j < 0 or i >= len(board) or j > len(board[0]):
                return
            if board[i][j] == 'O':
                board[i][j] = 'X'
                DFS(board, i + 1, j)
                DFS(board, i - 1, j)
                DFS(board, i, j + 1)
                DFS(board, i, j - 1)
        if len(board) == 0 or len(board) == 1 or len(board[0]) == 1:
            return None
        m = len(board)
        n = len(board[0])
        for j in range(n):
            if board[0][j] == 'O':
                DFSnot(board, 0, j)
        for j in range(n):
            if board[m - 1][j] == 'O':
                DFSnot(board, m - 1, j)
        for i in range(m):
            if board[i][0] == 'O':
                DFSnot(board, i, 0)
        for i in range(m):
            if board[i][n - 1] == 'O':
                DFSnot(board, i, n - 1)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    DFS(board, i, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == '$':
                    board[i][j] = 'O'
