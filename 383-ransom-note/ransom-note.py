#
# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return false. 
#
#
# Each letter in the magazine string can only be used once in your ransom note.
#
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
#
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
#
#


class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        l1 = list(ransomNote)
        l2 = list(magazine)
        for c in l1:
            if c in l2:
                l2.remove(c)
            else:
                return False
        return True
        
