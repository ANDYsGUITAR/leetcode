# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# Example:
#
#
# Input: 
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, trie, pre):
            if '#' in trie:
                self.ans.add(pre)
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return
            if not self.visited[i][j] and board[i][j] in trie:
                self.visited[i][j] = True
                dfs(board, i + 1, j, trie[board[i][j]], pre + board[i][j])
                dfs(board, i - 1, j, trie[board[i][j]], pre + board[i][j])
                dfs(board, i, j + 1, trie[board[i][j]], pre + board[i][j])
                dfs(board, i, j - 1, trie[board[i][j]], pre + board[i][j])
                self.visited[i][j] = False
        trie = {}
        for word in words:
            t = trie
            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.ans = set()
        self.visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(board, i, j, trie, '')
        return list(self.ans)
                
