# 668. Kth Smallest Number in Multiplication Table
# Hard

# 934

# 31

# Add to List

# Share
# Nearly everyone has used the Multiplication Table. The multiplication table of size m x n is an integer matrix mat where mat[i][j] == i * j (1-indexed).

# Given three integers m, n, and k, return the kth smallest element in the m x n multiplication table.

 

# Example 1:


# Input: m = 3, n = 3, k = 5
# Output: 3
# Explanation: The 5th smallest number is 3.
# Example 2:


# Input: m = 2, n = 3, k = 6
# Output: 6
# Explanation: The 6th smallest number is 6.
 

# Constraints:

# 1 <= m, n <= 3 * 104
# 1 <= k <= m * n


# This solution works:


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def helper(x):
            '''
            After we have the count of how many values in the table are 
            less than or equal to x, by the definition of helper(x), 
            we want to know if that count is greater than or equal to k.
            '''
            # just count how many elems are smaller than x by checking 
            # how many times we can divide
            count = 0
            for i in range(1, m+1):
                count += min(x // i, n)
            return count >= k

        lo, hi = 1, m * n
        while lo < hi:
            mi = (lo + hi) // 2
            if not helper(mi):
                lo = mi + 1
            else:
                hi = mi
        return lo