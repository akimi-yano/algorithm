'''
869. Reordered Power of 2
Solved
Medium
Topics
premium lock icon
Companies
You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
 

Constraints:

1 <= n <= 109
'''

from itertools import permutations

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        perm = permutations(string_num for string_num in str(n))
       
        for num_tup in list(perm):
            if num_tup[0] == '0':
                continue
            num = int(''.join(str_num for str_num in num_tup))
            if not(num & (num-1)):
                return True
        return False