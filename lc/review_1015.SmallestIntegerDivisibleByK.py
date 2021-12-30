# 1015. Smallest Integer Divisible by K
# Medium

# 440

# 437

# Add to List

# Share
# Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

# Return the length of n. If there is no such n, return -1.

# Note: n may not fit in a 64-bit signed integer.

 

# Example 1:

# Input: k = 1
# Output: 1
# Explanation: The smallest answer is n = 1, which has length 1.
# Example 2:

# Input: k = 2
# Output: -1
# Explanation: There is no such positive integer n divisible by 2.
# Example 3:

# Input: k = 3
# Output: 3
# Explanation: The smallest answer is n = 111, which has length 3.
 

# Constraints:

# 1 <= k <= 105


# This solution works:


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        # We just run the loop K times, 
        # check if the remainder is 0, and return -1 if not stopped.
        remainder = 0
        for length_N in range(1,K+1):
            remainder = (remainder*10+1) % K
            if remainder == 0:
                return length_N
        return -1