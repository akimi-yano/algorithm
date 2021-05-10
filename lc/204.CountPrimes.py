# 204. Count Primes
# Easy

# 3097

# 784

# Add to List

# Share
# Count the number of prime numbers less than a non-negative number, n.

 

# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0
 

# Constraints:

# 0 <= n <= 5 * 106

# This solution works:

class Solution:
    def countPrimes(self, n: int) -> int:
        '''
        Sieve of Eratosthenes algorithm
        1 make a table for all the numbers up to n
        2 i starts from 2 and while i*i < n (same as sqrt of n <- but we do this way so that we dont have to do expensive calc for math.sqrt) i = sqrt(n) then i*i = n
        3 if its prime them flip all its multipliers to be False up to n starting from i*i check one by one by doing j += i
        4 count all the Trues and return count
        '''
        if n <= 1:
            return 0
        primes = [True for _ in range(n)]
        primes[0] = primes[1] = False
        
        i = 2
        while i*i < n:
            if primes[i]:
                j = i*i
                while j < n:
                    primes[j] = False
                    j += i
            i+=1
        
        count = 0
        for i in range(2, n):
            if primes[i]:
                count += 1
        return count  