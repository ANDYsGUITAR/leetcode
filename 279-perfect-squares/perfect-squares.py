# -*- coding:utf-8 -*-


# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        queue = [0]
        visited = set(queue)
        step = 0
        while queue:
            tmp = []
            for q in queue:
                if q == n:
                    return step
                for ns in self.nextSum(n,q):
                    if ns in visited:
                        continue
                    visited.add(ns)
                    tmp.append(ns)
            queue = tmp
            step += 1
        
    
    def nextSum(self,n,q):
        k = int((n-q)**0.5)
        for i in range(1,k+1):
            yield i**2+q
