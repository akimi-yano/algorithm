# Excel Sheet Column Number

# Solution
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701
 

# Constraints:

# 1 <= s.length <= 7
# s consists only of uppercase English letters.
# s is between "A" and "FXSHRXW".

# solution 3 months ago:

class Solution:
    def titleToNumber(self, s: str) -> int:
        memo={}
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(alpha)):
            memo[alpha[i]]=i+1

        ans=0
        for i in range(len(s)):
            if s[i] in memo:
                ans += memo[s[i]]*26**(len(s)-1-i)
        return ans
    


# solution this time - 3 months after:

class Solution:
    def titleToNumber(self, s: str) -> int:
        total=0
        for i in range(len(s)-1,-1,-1):
            total+=((ord(s[i])-ord('A'))+1)*26**(len(s)-1-i)
        return total

# 543210 -> : big mid small
# 012345 <- : big mid small 
