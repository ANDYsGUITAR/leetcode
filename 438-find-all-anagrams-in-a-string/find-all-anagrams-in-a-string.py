# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
#
# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
#
# The order of output does not matter.
#
# Example 1:
#
# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]
#
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
#
#
#
# Example 2:
#
# Input:
# s: "abab" p: "ab"
#
# Output:
# [0, 1, 2]
#
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
#
#


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # if s is None:
        #     return []
        # if len(p) > len(s):
        #     return []
        # p = sorted(p)
        # l = len(p)
        # ans = []
        # for i in range(len(s) - l + 1):
        #     string = s[i : i+l]
        #     if sorted(string) == p:
        #         ans.append(i)
        # return ans
        
        from collections import Counter
        
        ans = []
        if len(p) > len(s):
            return ans
        pc = Counter(p)
        n = len(p)
        sc = Counter(s[:n - 1])
        for i in range(n - 1, len(s)):
            sc[s[i]] += 1
            if pc == sc:
                ans.append(i - n + 1)
            sc[s[i - n + 1]] -= 1
            if sc[s[i - n + 1]] == 0:
                del sc[s[i - n + 1]]
        return ans
        
