# 906. Super Palindromes
# Hard

# 223

# 316

# Add to List

# Share
# Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

# Given two positive integers left and right represented as strings, return the number of super-palindromes integers in the inclusive range [left, right].

 

# Example 1:

# Input: left = "4", right = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a palindrome.
# Example 2:

# Input: left = "1", right = "2"
# Output: 1
 

# Constraints:

# 1 <= left.length, right.length <= 18
# left and right consist of only digits.
# left and right cannot have leading zeros.
# left and right represent integers in the range [1, 1018].
# left is less than or equal to right.



# This solution works:

'''
generate palindrome efficuently by making half of it and copying the other half in reversed order
'''

class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left = int(left)
        right = int(right)
        count = 0
        current = 1
        while True:
            
            # odd digits
            c = str(current)
            p = int(c+c[:-1][::-1])
            if left <= (x := p * p) <= right and ((s := str(x)) == s[::-1]):
                count += 1
            if x > right:
                break
            
            # even digits
            c = str(current)
            p = int(c+c[::-1])
            if left <= (x := p * p) <= right and ((s := str(x)) == s[::-1]):
                count += 1
                
            current += 1
        return count