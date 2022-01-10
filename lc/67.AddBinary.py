# 67. Add Binary
# Easy

# 4000

# 472

# Add to List

# Share
# Given two binary strings a and b, return their sum as a binary string.

 

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.


# This solution works:


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        ans = []
        if len(a) < len(b):
            a, b = b, a
        j = len(a)-1
        for i in range(len(b)-1,-1,-1):
            carry, val = divmod((int(a[j])+int(b[i])+carry), 2)
            ans.append(str(val))
            j -= 1
 
        while j > -1:
            carry, val = divmod((int(a[j])+carry), 2)
            ans.append(str(val))
            j -= 1
            
        if carry:
            ans.append(str(carry))
        return "".join(reversed(ans))