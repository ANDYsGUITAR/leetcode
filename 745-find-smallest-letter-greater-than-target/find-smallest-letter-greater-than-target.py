#
# Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
#
# Letters also wrap around.  For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.
#
#
# Examples:
#
# Input:
# letters = ["c", "f", "j"]
# target = "a"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "c"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "d"
# Output: "f"
#
# Input:
# letters = ["c", "f", "j"]
# target = "g"
# Output: "j"
#
# Input:
# letters = ["c", "f", "j"]
# target = "j"
# Output: "c"
#
# Input:
# letters = ["c", "f", "j"]
# target = "k"
# Output: "c"
#
#
#
# Note:
#
# letters has a length in range [2, 10000].
# letters consists of lowercase letters, and contains at least 2 unique letters.
# target is a lowercase letter.
#
#


class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if ord(target) >= ord(letters[-1]):
            return letters[0]
        left = 0
        right = len(letters)-1
        while left+1 < right:
            mid = (left+right)//2
            if letters[mid] > target and letters[mid-1] <= target:
                return letters[mid]
            elif letters[mid] > target and letters[mid-1] > target:
                right = mid
            else:
                left = mid
        if letters[left] <= target < letters[right]:
            return letters[right]
        else:
            return letters[left]
            
