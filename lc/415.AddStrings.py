# 415. Add Strings
# Easy

# 1538

# 361

# Add to List

# Share
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.


# This solution works:
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        idx1 = len(num1)-1
        idx2 = len(num2)-1
        ans = 0
        carry = 0
        i = 0
        
        while idx1 > -1 and idx2 > -1:
            carry, val = divmod(int(num1[idx1]) + int(num2[idx2]) + carry, 10)
            ans += val*10**i
            idx1 -=1
            idx2 -=1
            i += 1
            
        while idx1 > -1:
            carry, val = divmod(int(num1[idx1]) + carry, 10)
            ans += val*10**i
            idx1 -=1
            i += 1
            
        while idx2 > -1:
            carry, val = divmod(int(num2[idx2]) + carry, 10)
            ans += val*10**i
            idx2 -=1
            i += 1
            
        if carry:
            ans += carry*10**i
            
        return str(ans)
    
# This solution works:

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []

        carry = 0
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        while p1 >= 0 or p2 >= 0:
            x1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            x2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            value = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            res.append(value)
            p1 -= 1
            p2 -= 1
        
        if carry:
            res.append(carry)
        
        return ''.join(str(x) for x in res[::-1])