# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
#
#  
#
#
#  
#
# Example:
#
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#  
#
# Note:
#
#
# 	You may use one character in the keyboard more than once.
# 	You may assume the input string will only contain letters of alphabet.
#
#


class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        l1 = sorted('qwertyuiop')
        l2 = sorted('asdfghjkl')
        l3 = sorted('zxcvbnm')
        l = [l1, l2, l3]
        ans = []
        for word in words:
            for s in l:
                if all(w in s for w in word.lower()):
                    ans.append(word)
        return ans
