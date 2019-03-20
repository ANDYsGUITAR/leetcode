# Given a string, find the length of the longest substring without repeating characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#
#
#
#


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1
        # if len(s) == 0:
        #     return 0
        # result = 1
        # n = len(s)
        # for i in range(n):
        #     j = i
        #     while j < len(s):
        #         if s[j] in s[i:j]:
        #             break
        #         else:
        #             j += 1
        #     result = max(j-i,result)
        # return result
        # 2
        # result = 0
        # left = 0
        # right = 0
        # n = len(s)
        # charList = []
        # while right < n:
        #     if s[right] not in charList:
        #         charList.append(s[right])
        #         right += 1
        #         result = max(result, len(charList))
        #     else:
        #         charList.pop(0)
        #         left += 1
        # return result
        start = max_length = 0
        dic = dict()

        for i, c in enumerate(s):
            if c in dic and start <= dic[c]:
                start = dic[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            dic[c] = i

        return max_length
