# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
#
#


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # TLE
        # ans = 0
        # for num in nums:
        #     curr = num
        #     tmp = 1
        #     while curr + 1 in nums:
        #         curr += 1
        #         tmp += 1
        #     ans = max(ans, tmp)
        # return ans
        
        nums.sort()
        if len(nums) == 0:
            return 0
        ans = 1
        curr = 1
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            elif nums[i] == nums[i-1]:
                pass
            else:
                ans = max(ans, curr)
                curr = 1
        ans = max(ans, curr)
        return ans
