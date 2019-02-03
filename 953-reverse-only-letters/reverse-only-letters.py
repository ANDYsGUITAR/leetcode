# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
#
#  
#
#
#
#
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: "ab-cd"
# Output: "dc-ba"
#
#
#
# Example 2:
#
#
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
#
#
# Example 3:
#
#
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
#
#
#  
#
#
# Note:
#
#
# 	S.length <= 100
# 	33 <= S[i].ASCIIcode <= 122 
# 	S doesn't contain \ or "
#
#
#
#
#


class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        indices = [i for i in range(len(S)) if S[i].isalpha()]
        reverse = indices[::-1]
        n = len(indices)
        ans = ''
        for i in range(len(S)):
            if i in indices:
                # need to reverse
                idx1 = indices.index(i)
                idx2 = reverse[idx1]
                ans += S[idx2]
            else:
                ans += S[i]
        return ans
