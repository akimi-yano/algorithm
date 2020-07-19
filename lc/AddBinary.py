#  Add Binary
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"
 

# Constraints:

# Each string consists only of '0' or '1' characters.
# 1 <= a.length, b.length <= 10^4
# Each string is either "0" or doesn't contain any leading zero.



# this  doesnt work - see below for a solution that works:

# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         ans = ""
#         length = min(len(a),len(b))
#         kuriage = 0
#         for i in range(length-1,-1,-1):
#             if a[i]+b[i]+kuriage>1:
#                 ans+=int(a[i])+int(b[i])+kuriage%2
#                 kuriage = 1
            
#             else:
#                 ans+=int(a[i])+int(b[i])+kuriage
#                 kuriage = 0
#         if length 


# this works !

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_idx = len(a)-1
        b_idx = len(b)-1
        ans = []
        kuriage = 0
        # start from the end of a & b and work backwards
        while a_idx>=0 and b_idx>=0:
            kuriage, val = divmod(int(a[a_idx])+int(b[b_idx])+kuriage,2)
            ans.append(val)
            a_idx-=1
            b_idx-=1
        # process any remaining elements in a
        while a_idx>=0:
            kuriage, val = divmod(int(a[a_idx])+kuriage,2)
            ans.append(val)
            a_idx-=1
        # process any remaining elements in b
        while b_idx>=0:
            kuriage, val = divmod(int(b[b_idx])+kuriage,2)
            ans.append(val)
            b_idx-=1
        # process carryover if there is one
        if kuriage !=0:
            ans.append(kuriage)
        ans.reverse()
        return "".join(str(ans[i]) for i in range(len(ans)))
        