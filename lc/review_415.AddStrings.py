# 415. Add Strings
# Easy

# 2172

# 428

# Add to List

# Share
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

# Example 1:

# Input: num1 = "11", num2 = "123"
# Output: "134"
# Example 2:

# Input: num1 = "456", num2 = "77"
# Output: "533"
# Example 3:

# Input: num1 = "0", num2 = "0"
# Output: "0"
 

# Constraints:

# 1 <= num1.length, num2.length <= 104
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.

# This solution works:

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        idx1 = len(num1)-1
        idx2 = len(num2)-1
        ans = []
        carry = total = 0
        
        while idx1 >= 0 and idx2 >= 0:
            carry, total = divmod(int(num1[idx1]) + int(num2[idx2]) + carry,10)
            ans.append(str(total))
            idx1 -= 1
            idx2 -= 1
            
        while idx1 >= 0:
            carry, total = divmod(int(num1[idx1]) + carry,10)
            ans.append(str(total))
            idx1 -= 1
        
        while idx2 >= 0:
            carry, total = divmod(int(num2[idx2]) + carry,10)
            ans.append(str(total))
            idx2 -= 1
        
        if carry:
            ans.append(str(carry))
        
        return "".join(reversed(ans))
        
            