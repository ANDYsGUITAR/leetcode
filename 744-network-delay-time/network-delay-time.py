# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
# Note:
#
#
# 	N will be in the range [1, 100].
# 	K will be in the range [1, N].
# 	The length of times will be in the range [1, 6000].
# 	All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
#
#
#  
#


class Solution:
    def networkDelayTime(self, times, n, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        N = [K] 
        S = [i for i in range(1, n+1) if i != K]
        d = {i: float('inf') for i in S}
        d[K] = 0
        mini = float('inf')
        for u, v, w in times:
            if u == K:
                d[v] = w
                if w < mini:
                    mini = w
                    memory = v
        if all(d[i] == float('inf') for i in S):
                return -1
        N.append(memory)
        S.remove(memory)
        while S:
            mini = float('inf')
            for u, v, w in times:
                if u == N[-1] and v not in N:
                    d[v] = min(d[v], d[u] + w)
            for x in S:
                if d[x] < mini:
                    mini = d[x]
                    memory = x
            if all(d[i] == float('inf') for i in S):
                return -1
            N.append(memory)
            S.remove(memory)
        return max(d.values())
        
        
