# There are N children standing in a line. Each child is assigned a rating value.
#
# You are giving candies to these children subjected to the following requirements:
#
#
# 	Each child must have at least one candy.
# 	Children with a higher rating get more candies than their neighbors.
#
#
# What is the minimum candies you must give?
#
# Example 1:
#
#
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
#
#
# Example 2:
#
#
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.
#
#


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0 or n == 1:
            return n
        left = [1 for _ in range(n)]
        right = [1 for _ in range(n)]
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
        ans = [max(left[i], right[i]) for i in range(n)]
        return sum(ans)
        # O(n^2)
        # n = len(ratings)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return 1
        # ans = [1 for _ in range(n)]
        # change = True
        # while change:
        #     change = False
        #     for i in range(n):
        #         if i <= n - 2 and ratings[i] > ratings[i + 1] and ans[i] <= ans[i + 1]:
        #             ans[i] = ans[i + 1] + 1
        #             change = True
        #         if i > 0 and ratings[i] > ratings[i - 1] and ans[i] <= ans[i - 1]:
        #             ans[i] = ans[i - 1] + 1
        #             change = True
        # return sum(ans)
