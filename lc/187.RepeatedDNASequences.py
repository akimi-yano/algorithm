# 187. Repeated DNA Sequences
# Medium

# 902

# 310

# Add to List

# Share
# All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

# Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

# Example 1:

# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]
# Example 2:

# Input: s = "AAAAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
 

# Constraints:

# 0 <= s.length <= 105
# s[i] is 'A', 'C', 'G', or 'T'.


# This solution works !!!
# Time: O(N) because the slicing part is always 10 which is constant
# Space: O(N) for dictionary 

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <10:
            return []
        memo = {}
        for i in range(len(s)):
            if i+10 > len(s):
                break
            sequence = s[i:i+10]
            if sequence not in memo:
                memo[sequence] = 1
            else:
                memo[sequence] += 1
        ans = []
        for k,v in memo.items():
            if v > 1:
                ans.append(k)
        return ans
    
