# Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.
#
# Example 1:
#
#
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
#
#
#  
#
# Note:
#
#
# 	S string length is in [1, 10000].
# 	C is a single character, and guaranteed to be in string S.
# 	All letters in S and C are lowercase.
#
#


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # # O(mn)
        # indices = [i for i in range(len(S)) if S[i] == C]
        # ans = []
        # for i in range(len(S)):
        #     min_dist = 100000
        #     for j in range(len(indices)):
        #         dist = abs(i - indices[j])
        #         if dist < min_dist:
        #             min_dist = dist
        #     ans.append(min_dist)
        # return ans
        
        ans = []
        prev = float('-inf')
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i-prev)
        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)
        return ans
            
        
