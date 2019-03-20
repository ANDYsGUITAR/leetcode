# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
#


class Solution:
    def nextPermutation(self, nums: 'List[int]') -> 'None':
        """
        Do not return anything, modify nums in-place instead.
        """
        # looking for the first decreasing number from backside
        n = len(nums)
        index = -1
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                break
        if index != -1:
            nums.append(float('-inf'))
            for i in range(index + 1, len(nums) - 1):
                if  nums[i] > nums[index] and nums[i + 1] <= nums[index]:
                    nums[index], nums[i] = nums[i], nums[index]
                    print(i)
                    nums.pop()
                    nums[index+1:] = sorted(nums[index+1:])
                    break
        else:
            nums[::] = nums[::-1]
            
