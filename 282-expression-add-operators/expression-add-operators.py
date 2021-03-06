# Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.
#
# Example 1:
#
#
# Input: num = "123", target = 6
# Output: ["1+2+3", "1*2*3"] 
#
#
# Example 2:
#
#
# Input: num = "232", target = 8
# Output: ["2*3+2", "2+3*2"]
#
# Example 3:
#
#
# Input: num = "105", target = 5
# Output: ["1*0+5","10-5"]
#
# Example 4:
#
#
# Input: num = "00", target = 0
# Output: ["0+0", "0-0", "0*0"]
#
#
# Example 5:
#
#
# Input: num = "3456237490", target = 9191
# Output: []
#
#


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        ans = []
        def recurse(index, prev_operand, current_operand, value, string):
            if index == N:
                if value == target and current_operand == 0:
                    ans.append(''.join(string[1:]))
                return
            current_operand = current_operand * 10 + int(num[index])
            str_op = str(current_operand)
            if current_operand > 0:
                recurse(index + 1, prev_operand, current_operand, value, string)
            string.append('+')
            string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop()
            string.pop()
            if string:

                # SUBTRACTION
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()

                # MULTIPLICATION
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])    
        return ans
