# 441. Arranging Coins
# Easy

# 1363

# 877

# Add to List

# Share
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1


# This solution works:


class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
         n = 5
         1
         23
         45
         ans = 2
         1,2,3
        '''
        i = 1
        ans = 0
        while n > 0:
            n -= i
            i += 1
            if n >= 0:
                ans += 1
        return ans


# This solution works - optimization:


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # formula: n*(n+1)//2
        left = 0
        right = n
        while left < right:
            mid = (left + right +1) // 2
            if mid*(mid+1)//2 <= n:
                left = mid
            else:
                right = mid -1
        return left


