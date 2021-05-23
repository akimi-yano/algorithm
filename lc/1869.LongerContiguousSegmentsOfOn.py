# 1869. Longer Contiguous Segments of Ones than Zeros
# Easy

# 12

# 0

# Add to List

# Share
# Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

# For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
# Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.

 

# Example 1:

# Input: s = "1101"
# Output: true
# Explanation:
# The longest contiguous segment of 1s has length 2: "1101"
# The longest contiguous segment of 0s has length 1: "1101"
# The segment of 1s is longer, so return true.
# Example 2:

# Input: s = "111000"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 3: "111000"
# The longest contiguous segment of 0s has length 3: "111000"
# The segment of 1s is not longer, so return false.
# Example 3:

# Input: s = "110100010"
# Output: false
# Explanation:
# The longest contiguous segment of 1s has length 2: "110100010"
# The longest contiguous segment of 0s has length 3: "110100010"
# The segment of 1s is not longer, so return false.
 

# Constraints:

# 1 <= s.length <= 100
# s[i] is either '0' or '1'.


# This solution works:


class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        best1 = 0
        best0 = 0
        ones = 0
        zeros = 0
        isOne = None
        if s[0] == '1':
            isOne = True
            ones += 1
        else:
            isOne = False
            zeros += 1
           
        for i in range(1, len(s)):
            if s[i] == '1':
                if isOne == False:
                    isOne = True
                    zeros = 0
                ones += 1
            else:
                if isOne == True:
                    isOne = False
                    ones = 0
                zeros += 1
            best1 = max(best1, ones)
            best0 = max(best0, zeros)
        
        best1 = max(best1, ones)
        best0 = max(best0, zeros)
        return best1 > best0
            
