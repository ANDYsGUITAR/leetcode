# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
#
# Example 1:
#
#
# Input: "aacecaaa"
# Output: "aaacecaaa"
#
#
# Example 2:
#
#
# Input: "abcd"
# Output: "dcbabcd"


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def center_odd(s):
            mid = len(s) // 2
            while mid != 0:
                if s[:mid] == s[mid + 1 : mid + 1 + mid][::-1]:
                    return mid
                else:
                    mid -= 1
            return mid
        def center_even(s):
            mid = len(s) // 2
            while mid != 0 and s[mid] != s[mid + 1]:
                mid -= 1
            while mid != 0:
                if s[:mid] == s[mid + 2 : mid + 2 + mid][::-1] and s[mid] == s[mid + 1]:
                    return mid
                else:
                    mid -= 1
            return mid if s[mid] == s[mid + 1] else -1
        
        if not s or s == s[::-1]:
            return s
        if len(s) == 2:
            return s[-1] + s
        odd = center_odd(s)
        even = center_even(s)
        print(odd, even)
        odd_ans = s[odd + 1:][::-1] + s[odd] + s[odd + 1:]
        if even != -1:
            even_ans = s[even + 2:][::-1] + s[even] + s[even + 1] + s[even + 2:]
        else:
            return odd_ans
        return odd_ans if len(odd_ans) < len(even_ans) else even_ans
