# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
#
# Example 1:
#
#
# Input: "3+2*2"
# Output: 7
#
#
# Example 2:
#
#
# Input: " 3/2 "
# Output: 1
#
# Example 3:
#
#
# Input: " 3+5 / 2 "
# Output: 5
#
#
# Note:
#
#
# 	You may assume that the given expression is always valid.
# 	Do not use the eval built-in library function.
#


class Solution:
    def calculate(self, s: str) -> int:
        s += '+0'
        stack = []
        num = 0
        preOp = '+'
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif not c.isspace():
                if preOp == '+':
                    stack.append(num)
                elif preOp == '-':
                    stack.append(-num)
                elif preOp == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                preOp = c
                num = 0
        return sum(stack)
