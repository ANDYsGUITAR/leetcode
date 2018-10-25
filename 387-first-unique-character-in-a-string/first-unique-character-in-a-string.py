#
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
#
# s = "leetcode"
# return 0.
#
# s = "loveleetcode",
# return 2.
#
#
#
#
# Note: You may assume the string contain only lowercase letters.
#


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for c in s:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1
        for c in s:
            if dic[c] == 1:
                return s.index(c)
        return -1
