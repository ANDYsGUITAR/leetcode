# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#
#


class Solution:
    def numTrees(self, n: int) -> int:
        '''
        use dynamic programme
        dp[n] means the number of unique bst's 
        that store values 1...n 
        then if we use i as root node, we have F(i, n) trees
        then  root's left has i - 1 nodes,
        root's right has n - i nodes
        so F(i, n) = dp(i - 1) * dp(n - i)
        dp(n) = dp(0)dp(n - 1) + ... + dp(n - 1)dp(0)
        '''
        
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]
