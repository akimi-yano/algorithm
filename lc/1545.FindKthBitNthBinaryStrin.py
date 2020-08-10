# 1545. Find Kth Bit in Nth Binary String
# Medium

# 64

# 5

# Add to List

# Share
# Given two positive integers n and k, the binary string  Sn is formed as follows:

# S1 = "0"
# Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first 4 strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

# Example 1:

# Input: n = 3, k = 1
# Output: "0"
# Explanation: S3 is "0111001". The first bit is "0".
# Example 2:

# Input: n = 4, k = 11
# Output: "1"
# Explanation: S4 is "011100110110001". The 11th bit is "1".
# Example 3:

# Input: n = 1, k = 1
# Output: "0"
# Example 4:

# Input: n = 2, k = 3
# Output: "1"
 

# Constraints:

# 1 <= n <= 20
# 1 <= k <= 2n - 1


# this solution works !   

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n):
            temp = ""
            for c in range(len(s)-1,-1,-1):
                if s[c]=="1":
                    temp+="0"
                else:
                    temp+="1"
            s=s+"1"+temp
        return s[k-1]
'''     
S1 = "0"
Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and 
invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first 4 strings in the above sequence are:

S1 = "0"
S2 = "011"
S3 = "0111001"
S4 = "011100110110001"


0 1 1

'''

# tried with list comprehension !!!!

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s="0"
        for i in range(n):
            s=s+"1"+''.join(['0' if s[c]=='1' else '1' for c in range(len(s)-1,-1,-1)]) 
        return s[k-1]