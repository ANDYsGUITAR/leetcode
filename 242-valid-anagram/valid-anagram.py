# Given two strings s and t , write a function to determine if t is an anagram of s.
#
# Example 1:
#
#
# Input: s = "anagram", t = "nagaram"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "rat", t = "car"
# Output: false
#
#
# Note:
# You may assume the string contains only lowercase alphabets.
#
# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
#


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        c1 = collections.Counter(s)
        c2 = collections.Counter(t)
        return c1 == c2
        # if len(s) != len(t):
        #     return False
        # s_dict = dict()
        # t_dict = dict()
        # for c in s:
        #     if c in s_dict:
        #         s_dict[c] += 1
        #     else:
        #         s_dict[c] = 1
        # for c in t:
        #     if c in t_dict:
        #         t_dict[c] += 1
        #     else:
        #         t_dict[c] = 1
        # if s_dict == t_dict:
        #     return True
        # else:
        #     return False
        
