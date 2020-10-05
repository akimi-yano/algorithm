# 1009. Complement of Base 10 Integer
# Easy

# 327

# 38

# Add to List

# Share
# Every non-negative integer N has a binary representation.  For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.  Note that except for N = 0, there are no leading zeroes in any binary representation.

# The complement of a binary representation is the number in binary you get when changing every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

# For a given number N in base-10, return the complement of it's binary representation as a base-10 integer.


# Example 1:

# Input: 5
# Output: 2
# Explanation: 5 is "101" in binary, with complement "010" in binary, which is 2 in base-10.
# Example 2:

# Input: 7
# Output: 0
# Explanation: 7 is "111" in binary, with complement "000" in binary, which is 0 in base-10.
# Example 3:

# Input: 10
# Output: 5
# Explanation: 10 is "1010" in binary, with complement "0101" in binary, which is 5 in base-10.

# Note:

# 0 <= N < 10^9
# This question is the same as 476: https://leetcode.com/problems/number-complement/




# This solution works ! : - string
    
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        s = bin(N)[2:]
        ans = ""
        for i in range(len(s)):
            if s[i] == '1':
                ans += '0'
            else:
                ans += '1'
        return int(ans, base=2)


# This solution  works ! : - bitwise + power
    
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        
        # find the highest bit with 1
        i = 0
        while N >> i > 0:
            i += 1
        
        i-=1
        ans = 0 
        while i >= 0:
            if (((N >> i) &1)^1):
                ans+=2**i
            i-=1   
        return ans
    
    
# This solution works !

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        r = 0
        for x in bin(N)[2:]:
            r <<= 1
            x = int(x)
            r += (x^1)
        return r
    
# This solution works !
'''
111
^
010
=
101
or count how many bits we have by doing len(bin(N)-2 
we need to do -2 because the first 2 of the length are not bits 
and to fill all with 1 we just bit shift 1 to right by the times of length and -1 
we just xor 
edge case if when N=0 we return 1
'''
class Solution:
    def bitwiseComplement(self, N: int) -> int:

        return 1 if N ==0 else ( ( 1 << (len(bin(N)) -2) ) -1) ^ N
    
    
# Another solution that works !
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1
        res = 0
        factor = 1
        while N:
            res += factor * (1 if N%2 == 0 else 0)
            factor *= 2
            N //=2
        return res