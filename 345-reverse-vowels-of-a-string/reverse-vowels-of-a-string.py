# Write a function that takes a string as input and reverse only the vowels of a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#  
#


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        indices = [i for i in range(len(s)) if s[i] in vowels]
        reverse = indices[::-1]
        m = zip(indices, reverse)
        ans = list(s)
        l = len(indices)
        count = 0
        for i, j in m:
            print(i, j)
            count += 1
            ans[i], ans[j] = ans[j], ans[i]
            if count == l // 2:
                break
        return ''.join(a for a in ans)
        
