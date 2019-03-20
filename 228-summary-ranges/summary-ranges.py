# Given a sorted integer array without duplicates, return the summary of its ranges.
#
# Example 1:
#
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#
#
# Example 2:
#
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
#
#


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n == 1:
            return [str(x) for x in nums]
        start, end = 0, 1
        ans = []
        while end <= n - 1:
            if nums[end] - nums[end - 1] == 1:
                end += 1
            else:
                if end - 1 == start:
                    ans.append(str(nums[start]))
                    start = end
                    end = end + 1
                else:
                    ans.append(str(nums[start]) + "->"+ str(nums[end - 1]))
                    start = end
                    end = end + 1
        if start == n - 1:
            ans.append(str(nums[start]))
        else:
            ans.append(str(nums[start]) + "->"+ str(nums[end - 1]))
        return ans
        
