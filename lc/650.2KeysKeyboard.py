# 650. 2 Keys Keyboard
# Medium

# 1661

# 119

# Add to List

# Share
# Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

# Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
# Paste: You can paste the characters which are copied last time.
 

# Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

# Example 1:

# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.
 

# Note:

# The n will be in the range [1, 1000].

# This solution works:

class Solution:
    def minSteps(self, n: int) -> int:
        @lru_cache(None)
        def helper(total, cur):
            nonlocal n
            if total == n:
                return 0
            if total > n or cur > 1000:
                return float('inf')
            
            min_ops = float('inf')
            # copy all - copy only if total is not equal to cur (cur we copied but did not paste, it means a potential risk of endless copying)
            if total != cur:
                min_ops = min(min_ops, 1 + helper(total, total))
            
            # paste - paste only if cur is not 0 (means has not copied at all)
            if cur > 0:
                min_ops = min(min_ops, 1 + helper(total + cur, cur))
            return min_ops
            
        return helper(1, 0)