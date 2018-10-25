# Given an array of strings, group anagrams together.
#
# Example:
#
#
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
#
# Note:
#
#
# 	All inputs will be in lowercase.
# 	The order of your output does not matter.
#
#


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
            sort = ''.join(sorted(s))
            if sort in dic:
                dic[sort].append(s)
            else:
                dic[sort] = [s]
        result = []
        for key in dic:
            result.append(dic[key])
        return result
        
