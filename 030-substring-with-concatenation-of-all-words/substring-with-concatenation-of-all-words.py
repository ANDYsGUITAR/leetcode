# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# Example 1:
#
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
#
#
# Example 2:
#
#
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []
#
#


class Solution:
    def findSubstring(self, s: 'str', words: 'List[str]') -> 'List[int]':
        if len(words) == 0 or len(s) == 0:
            return []
        wordDict = {}
        for word in words:
            wordDict[word] = wordDict.get(word, 0) + 1
        n, m, k = len(s), len(words[0]), len(words)
        ans = []
        for i in range(n - m*k + 1):
            count = 0
            currDict = {}
            while count < k:
                word = s[i + m * count : i + m * (count + 1)]
                if word not in wordDict:
                    break
                currDict[word] = currDict.get(word, 0) + 1
                if currDict[word] > wordDict[word]:
                    break
                count += 1
            if count == k:
                ans.append(i)
        return ans
