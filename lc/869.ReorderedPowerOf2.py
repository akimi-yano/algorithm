# 869. Reordered Power of 2
# Medium

# 356

# 122

# Add to List

# Share
# Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

# Return true if and only if we can do this in a way such that the resulting number is a power of 2.

 

# Example 1:

# Input: 1
# Output: true
# Example 2:

# Input: 10
# Output: false
# Example 3:

# Input: 16
# Output: true
# Example 4:

# Input: 24
# Output: false
# Example 5:

# Input: 46
# Output: true
 

# Note:

# 1 <= N <= 10^9

# This solution works:

from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        all_options = []
        for i in range(33):
            val = 2**i
            counts = Counter()
            while val:
                val, remainder = divmod(val, 10)
                counts[remainder] += 1
            all_options.append(counts)
        
        counts = Counter()
        while N:
            N, remainder = divmod(N, 10)
            counts[remainder] += 1
        
        for count_dict in all_options:
            if count_dict == counts:
                return True
        return False
            
# This solution works - optimization by storing all the options in class variable without 'self' (instead of instance variable):

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
            