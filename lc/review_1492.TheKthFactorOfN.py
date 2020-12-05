# 1492. The kth Factor of n
# Medium

# 210

# 89

# Add to List

# Share
# Given two positive integers n and k.

# A factor of an integer n is defined as an integer i where n % i == 0.

# Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

 

# Example 1:

# Input: n = 12, k = 3
# Output: 3
# Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.
# Example 2:

# Input: n = 7, k = 2
# Output: 7
# Explanation: Factors list is [1, 7], the 2nd factor is 7.
# Example 3:

# Input: n = 4, k = 4
# Output: -1
# Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
# Example 4:

# Input: n = 1, k = 1
# Output: 1
# Explanation: Factors list is [1], the 1st factor is 1.
# Example 5:

# Input: n = 1000, k = 3
# Output: 4
# Explanation: Factors list is [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000].
 

# Constraints:

# 1 <= k <= n <= 1000


# This solution works !:

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        if n <= 0:
            return -1
        cur = 1
        i = 1 
        while cur < k:
            i += 1
            if n % i == 0:
                cur +=  1
            if i > n:
                return -1
            if cur == k:
                return i
        
        if cur == k:
            return i
        else:
            return -1



# more optimal solution: we can check only divisors which are less than square root of n: 
# each of them will have pair: for any d divisor of n, number n/d is also divisor of n. 
# There is one exception, when d = n/d and we do not have pair. 
# Let us find all factors before square root of n and put the into list, 
# and also put all divisors which are after square root of n to another list. 
# Then we combine these two lists and return element number k.

# Complexity: time and space complexity is O(sqrt(n)), because there will be at most 2*sqrt(n) factors of n.

class Solution:
    def kthFactor(self, n, k):
        f1, f2 = [], []
        for s in range(1, int(sqrt(n)) + 1 ):
            if n % s == 0:
                f1 += [s]
                f2 += [n//s]
                
        if f1[-1] == f2[-1]: f2.pop()
            
        factors = f1 + f2[::-1]
        return -1 if len(factors) < k else factors[k-1]
    
# it works before they come as a pair so put both of them into array
# until square root of that number
# if the last numbers are the same, only append one of them
# put together the array and return 