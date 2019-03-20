# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation: 
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation: 
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
#


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        def helper(x, y, op):
            if op == '+':
                return int(x) + int(y)
            elif op == '-':
                return int(x) - int(y)
            else:
                return int(x) * int(y)
            
        if input.isdigit():
            return [int(input)]
        ans = []
        for i in range(len(input)):
            if input[i] in '+-*':
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        ans.append(helper(l, r, input[i]))
        return ans
