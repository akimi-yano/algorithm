# 869. Reordered Power of 2
# Medium

# 913

# 239

# Add to List

# Share
# You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this so that the resulting number is a power of two.

 

# Example 1:

# Input: n = 1
# Output: true
# Example 2:

# Input: n = 10
# Output: false
 

# Constraints:

# 1 <= n <= 109


# This solution works:


from collections import Counter
class Solution:
    def helper():
        all_options = []
        for i in range(33):
            val = 2**i
            counts = Counter()
            while val:
                val, remainder = divmod(val, 10)
                counts[remainder] += 1
            all_options.append(counts)
        return all_options

    all_options = helper()
    
    def reorderedPowerOf2(self, N: int) -> bool:
        
        counts = Counter()
        while N:
            N, remainder = divmod(N, 10)
            counts[remainder] += 1
        
        for count_dict in Solution.all_options:
            if count_dict == counts:
                return True
        return False
            