'''
67. Add Binary
Easy
Topics
Companies
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = []
        a_i = len(a)-1
        b_i = len(b)-1
        carry = 0
        while a_i > -1 and b_i > -1:
            carry, val = divmod(int(a[a_i]) + int(b[b_i]) + carry, 2)
            ans.append(str(val))
            a_i -= 1
            b_i -= 1
        
        while a_i > -1:
            carry, val = divmod(int(a[a_i]) + carry, 2)
            ans.append(str(val))
            a_i -= 1
           
        while b_i > -1:
            carry, val = divmod(int(b[b_i]) + carry, 2)
            ans.append(str(val))
            b_i -= 1
        
        if carry:
            ans.append(str(carry))
        
       
        ans = ''.join(reversed(ans))
        return ans

# Time: O(a+b)
# Space: O(max(a,b)) 