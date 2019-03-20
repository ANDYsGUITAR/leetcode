# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
#
# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.
#
# Example:
#
#
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
#
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
#
#


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = collections.defaultdict(int)
        for i in range(len(s)):
            seq[s[i : i + 10]] += 1
        return [key for key, value in seq.items() if value > 1]
