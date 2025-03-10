# 926. Flip String to Monotone Increasing
# Medium

# 1160

# 35

# Add to List

# Share
# A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

# Return the minimum number of flips to make s monotone increasing.

 

# Example 1:

# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
# Example 2:

# Input: s = "010110"
# Output: 2
# Explanation: We flip to get 011111, or alternatively 000111.
# Example 3:

# Input: s = "00011000"
# Output: 2
# Explanation: We flip to get 00000000.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either '0' or '1'.

# This solution works:

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @lru_cache(None)
        def helper(i, prev):
            if i > len(s)-1:
                return 0
            min_op = len(s)
            if prev is None:
                if s[i] == '0':
                    min_op = min(min_op, helper(i+1, '0'), 1+helper(i+1, '1'))
                else:
                    min_op = min(min_op, helper(i+1, '1'), 1+helper(i+1, '0'))
            elif prev == '0':
                if s[i] == '0':
                    min_op = min(min_op, helper(i+1, '0'), 1+helper(i+1, '1'))
                else:
                    min_op = min(min_op, helper(i+1, '1'), 1+helper(i+1, '0'))
            else:
                if s[i] == '0':
                    min_op = min(min_op, 1+helper(i+1, '1'))
                else:
                    min_op = min(min_op, helper(i+1, '1'))
            return min_op
                
        return helper(0, None)


# This solution works: - optimization:

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @lru_cache(None)
        def helper(i, prev):
            if i > len(s)-1:
                return 0
            min_op = len(s)
            if prev == '0':
                if s[i] == '0':
                    min_op = helper(i+1, '0')
                else:
                    min_op = min(min_op, helper(i+1, '1'), 1+helper(i+1, '0'))
            else:
                if s[i] == '0':
                    min_op = 1+helper(i+1, '1')
                else:
                    min_op = helper(i+1, '1')
            return min_op
                
        return helper(0, '0')