# 60. Permutation Sequence
# Medium

# 1402

# 315

# Add to List

# Share
# The set [1,2,3,...,n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

# Note:

# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# Example 1:

# Input: n = 3, k = 3
# Output: "213"
# Example 2:

# Input: n = 4, k = 9
# Output: "2314"
# Accepted
# 176,951
# Submissions
# 489,532

import math
class Solution:
    
# he idea is as follow:

# For permutations of n, the first (n-1)! permutations start with 1, next (n-1)! ones start with 2, ... and so on. And in each group of (n-1)! permutations, the first (n-2)! permutations start with the smallest remaining number, ...

# take n = 3 as an example, the first 2 (that is, (3-1)! ) permutations start with 1, next 2 start with 2 and last 2 start with 3. For the first 2 permutations (123 and 132), the 1st one (1!) starts with 2, which is the smallest remaining number (2 and 3). So we can use a loop to check the region that the sequence number falls in and get the starting digit. Then we adjust the sequence number and continue.


    def getPermutation(self, n: int, k: int) -> str:
        numbers = range(1, n+1)
        permutation = ''
        k -= 1
        while n > 0:
            n -= 1
            # get the index of current digit
            index, k = divmod(k, math.factorial(n))
            permutation += str(numbers[index])
            # remove handled number
            numbers.remove(numbers[index])

        return permutation
        # n = 2
        # 2!
        # 12
        # 21
        
        # 3! = 3*2 = 6
        # 4! = 4*3*2 = 24
        # n : digits
        
        # 1 1234 ordered
        # 2 1243
        # 3 1324
        # 4 1342
        # 5 1423
        # 6 1432 reversed
        
        # 7 2134
        # 8 2143
        # 9 2314
        
        # n = 5
        # k = 5
        # 1 12345
        # 2 12354
        # 3 12435
        # 4 12453
        # 5 12534
        

# love this Solution!!!
 def getPermutation(self, n, k):
        def helper(s, k_left):
            if len(s) < 2:
                return s
            i = 0
            sub_factorial = math.factorial(len(s)-1)
            while sub_factorial < k_left:
                k_left -= sub_factorial
                i += 1
            chosen_letter = s[i]
            s_remaining = s[:i] + s[i+1:]
            return chosen_letter + helper(s_remaining, k_left)

        n_str = ''.join([str(i) for i in range(1, n+1)])
        return helper(n_str, k)
        