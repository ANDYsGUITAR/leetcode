# In a string S of lowercase letters, these letters form consecutive groups of the same character.
#
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
#
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
#
# The final answer should be in lexicographic order.
#
#  
#
# Example 1:
#
#
# Input: "abbxxxxzzy"
# Output: [[3,6]]
# Explanation: "xxxx" is the single large group with starting  3 and ending positions 6.
#
#
# Example 2:
#
#
# Input: "abc"
# Output: []
# Explanation: We have "a","b" and "c" but no large group.
#
#
# Example 3:
#
#
# Input: "abcdddeeeeaabbbcd"
# Output: [[3,5],[6,9],[12,14]]
#
#  
#
# Note:  1 <= S.length <= 1000
#


class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start = end = 0
        ans = []
        while start < len(S) - 2 and end < len(S) - 1:
            if S[end] == S[end + 1]:
                end += 1
                print(end)
            else:
                l = end - start + 1
                if l >= 3:
                    ans.append([start, end])
                start = end + 1
                end = start
        if end - start + 1 >= 3:
            ans.append([start, end])
        return ans
            
