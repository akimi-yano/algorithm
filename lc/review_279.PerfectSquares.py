# 279. Perfect Squares
# Medium

# 5369

# 256

# Add to List

# Share
# Given an integer n, return the least number of perfect square numbers that sum to n.

# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

# Example 1:

# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
 

# Constraints:

# 1 <= n <= 104


# This solution works:


'''
First of all, there is a statement that any number can be represented as sum of 4 squares:
https://en.wikipedia.org/wiki/Lagrange's_four-square_theorem. So, answer always will be 4? No, when we talk about 4 squares, it means that some of them can be equal to zero. So, we have 4 options: either 1, 2, 3 or 4 squares and we need to choose one of these numbers.

How to check if number is full square? Just compare square of integer part of root and this number. Complexity of this part is O(1).
How to check if number is sum of 2 squares: n = i*i + j*j? iterate ovell all i < sqrt(n) and check that n - i*i is full square. Complexity of this part is O(sqrt(n)).
How to check that number is sum of 4 squares? In the same link for wikipedia:
by proving that a positive integer can be expressed as the sum of three squares if and only if it is not of the form 4^k(8m+7) for integers k and m. So, what we need to do is to check this condition and return true if it fulfilled. Complexity is O(log n)
Do we need to check anything else? No, because we have only one options left: 3 squares.
Complexity: time complexity is O(sqrt(n)) and space complexity is O(1).
'''
class Solution:
    def numSquares(self, n):
        if int(sqrt(n))**2 == n: return 1
        for j in range(int(sqrt(n)) + 1):
            if int(sqrt(n - j*j))**2 == n - j*j: return 2
            
        while n % 4 == 0: 
            n >>= 2
        if n % 8 == 7: return 4
        return 3
    
