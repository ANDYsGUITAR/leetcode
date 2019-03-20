# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
#
# Input: [3,2,3]
# Output: [3]
#
# Example 2:
#
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
#


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # moore
        num1 = None
        num2 = None
        count1 = count2 = 0
        for num in nums:
            if num == num1:
                count1 += 1
            elif num == num2:
                count2 += 1
            elif count1 == 0:
                num1, count1 = num, 1
            elif count2 == 0:
                num2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        ans = []
        maj = len(nums) // 3
        if nums.count(num1) > maj:
            ans.append(num1)
        if nums.count(num2) > maj:
            ans.append(num2)
        return ans
                
#         n = len(nums)
#         maj = n // 3
#         dic = {}
#         ans = set()
#         for num in nums:
#             if dic.get(num, 0) > maj:
#                 continue
#             else:
#                 dic[num] = dic.get(num, 0) + 1
            
#                 if dic[num] > maj:
#                     ans.add(num)
#         return list(ans)

