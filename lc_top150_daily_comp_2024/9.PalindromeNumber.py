'''
9. Palindrome Number
Solved
Easy
Topics
Companies
Hint
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
'''

# This approach works:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = 0
        original_x = x
        while x:
            x, val = divmod(x, 10)
            reversed_x *= 10
            reversed_x += val

        return reversed_x == original_x

# Time: O(N) where N is the number of digit of x
# Space: O(1)

# This approach is a slight optimization by reversing only half

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # this approach only reverses the half and if its odd, dont check the middle
        # immediately return false if x is negative or leading 0
        if x < 0 or (x!=0 and x%10 == 0):
            return False
        reversed_x = 0
        while x > reversed_x:
            x, val = divmod(x, 10)
            reversed_x *= 10
            reversed_x += val

        return reversed_x == x or reversed_x//10 == x
    
# Time: O(N)
# Spce: O(1)