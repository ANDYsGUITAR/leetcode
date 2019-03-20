#
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# For example, given n = 3, a solution set is:
#
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
#


class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        
        ans = []
        def backtrack(s, left, right):
            if len(s) == n * 2:
                ans.append(s)
            else:
                if left < n:
                    backtrack(s + '(', left + 1, right)
                if right < left:
                    backtrack(s + ')', left, right + 1)
        backtrack('', 0, 0)
        return ans
