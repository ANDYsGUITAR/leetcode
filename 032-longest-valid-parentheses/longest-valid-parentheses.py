# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
# Example 1:
#
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
#
# Example 2:
#
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
#
#


class Solution:
    def longestValidParentheses(self, s: 'str') -> 'int':
        
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')' and s[i - 1] == '(':
                if i >= 2:
                    dp[i] = dp[i - 2] + 2
                else:
                    dp[i] = 2
            elif s[i] == ')' and s[i - 1] == ')':
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
        print(dp)
        return max(dp)
        
        
        # TLE
#         def Pnum(s):
#             count = left = right = 0
#             for c in s:
#                 if c == '(':
#                     left += 1
#                 else:
#                     if left != 0:
#                         left -= 1
#                         count += 1
#                     else:
#                         right += 1
#             return count
        
#         def length(s):
#             return len(s) if Pnum(s) * 2 == len(s) else 0
        
#         if len(s) % 2 == 0:
#             l = len(s)
#         else:
#             l = len(s) - 1
#         ans = 0
#         while l >= 2:
#             for i in range(len(s) - l + 1):
#                 ans = length(s[i : i+l])
#                 if ans > 0:
#                     break
#             if ans > 0:
#                 break
#             else:
#                 l -= 2
#         return ans

            
        
