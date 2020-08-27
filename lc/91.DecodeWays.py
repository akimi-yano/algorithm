# 91. Decode Ways

# A message containing letters from A-Z is being encoded to numbers using the following mapping:

# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given a non-empty string containing only digits, determine the total number of ways to decode it.

# Example 1:

# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
# Example 2:

# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).




# THIS SOLUTION WORKS:
    
class Solution:
    def numDecodings(self, s: str) -> int:
        dic = {}
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i,char in enumerate(chars):
            dic[str(i+1)] = char
            
        memo = {}
        def helper(i):
            if i in memo:
                return memo[i]
            if i>len(s)-1:
                return 1
            ways = 0
            # one letter or two letters
            if s[i] in dic:
                ways+=helper(i+1)
            if i<=len(s)-2 and s[i:i+2] in dic:
                ways+=helper(i+2)
            memo[i] = ways
            return ways
        return helper(0)
        









# TEST
# s = "123"
# i=1
# print(s[i:i+2])
