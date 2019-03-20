# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
#
#
# Example 2:
#
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
#


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        change = False
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr.start > newInterval.start:
                intervals = intervals[:i] + [newInterval] + intervals[i:]
                change = True
                break
        if not change:
            intervals.append(newInterval)
        # tmp = [[i.start, i.end] for i in intervals]
        # print(tmp)
        n = len(intervals)
        if n <= 1:
            return intervals
        stack = [intervals[0]]
        ans = []
        for i in range(1, n):
            prev = stack[-1]
            curr = intervals[i]
            if curr.start > prev.end:
                ans.append(prev)
                stack.pop()
                stack.append(curr)
            else:
                new = Interval()
                new.start = prev.start
                new.end = max(prev.end, curr.end)
                stack.pop()
                stack.append(new)
        ans.append(stack[-1])
        return ans
        
            
            
