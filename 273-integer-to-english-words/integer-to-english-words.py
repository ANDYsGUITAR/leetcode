# Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.
#
# Example 1:
#
#
# Input: 123
# Output: "One Hundred Twenty Three"
#
#
# Example 2:
#
#
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
#
# Example 3:
#
#
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
#
#
# Example 4:
#
#
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
#
#


class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
           'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
        tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()
        def word(num):
            if num < 20:
                return to19[num - 1 : num]
            if num < 100:
                return [tens[num // 10 - 2]] + word(num % 10)
            if num < 1000:
                return [to19[num // 100 - 1]] + ['Hundred'] + word(num % 100)
            for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if num < 1000 ** (p + 1):
                    return word(num // (1000 ** p)) + [w] + word(num % (1000 ** p))
        return ' '.join(word(num)) if word(num) else 'Zero'
#         def parse(num):
#             num = str(num)
#             l = len(num)
#             result = []
#             if l % 3 == 0:
#                 for i in range(l // 3):
#                     result.append(num[i * 3:i * 3 + 3])
#             else:
#                 r = l % 3
#                 result.append(num[:r])
#                 for i in range(l // 3):
#                     result.append(num[r + i * 3: r + i * 3 + 3])
#             return result
        
#         p = parse(num)
#         print(p)
                
