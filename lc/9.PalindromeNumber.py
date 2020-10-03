# 9. Palindrome Number
# Easy

# 2596

# 1609

# Add to List

# Share
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Could you solve it without converting the integer to a string?



# This solution works but I think we should all try to solve it without casting it to  string:
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        
        for i in range(len(x_str)):
            if x_str[i] != x_str[len(x_str)-1-i]:
                return False 
        return True
            
            

# This solution works ! without casting it to string !:
'''
write down / walk through an example to debug
'''
class Solution:
    def isPalindrome(self, x: int) -> bool: 
        if x<0:
            return False
        
        digits = 0
        temp = x
        
        while temp:
            temp //= 10
            digits += 1
            
        for i in range(digits//2):
            small = x % 10  
            large = x
            
            for _ in range(digits-1):
                large //= 10
            large %= 10
            
            if small != large:
                return False
            x //= 10
            
            digits -= 2
        return True