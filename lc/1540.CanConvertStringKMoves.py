# 1540. Can Convert String in K Moves
# User Accepted:2323
# User Tried:3503
# Total Accepted:2366
# Total Submissions:11363
# Difficulty:Medium
# Given two strings s and t, your goal is to convert s into t in k moves or less.

# During the ith (1 <= i <= k) move you can:

# Choose any index j (1-indexed) from s, such that 1 <= j <= s.length and j has not been chosen in any previous move, and shift the character at that index i times.
# Do nothing.
# Shifting a character means replacing it by the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Shifting a character by i means applying the shift operations i times.

# Remember that any index j can be picked at most once.

# Return true if it's possible to convert s into t in no more than k moves, otherwise return false.

 

# Example 1:

# Input: s = "input", t = "ouput", k = 9
# Output: true
# Explanation: In the 6th move, we shift 'i' 6 times to get 'o'. And in the 7th move we shift 'n' to get 'u'.
# Example 2:

# Input: s = "abc", t = "bcd", k = 10
# Output: false
# Explanation: We need to shift each character in s one time to convert it into t. We can shift 'a' to 'b' during the 1st move. However, there is no way to shift the other characters in the remaining moves to obtain t from s.
# Example 3:

# Input: s = "aab", t = "bbb", k = 27
# Output: true
# Explanation: In the 1st move, we shift the first 'a' 1 time to get 'b'. In the 27th move, we shift the second 'a' 27 times to get 'b'.
 

# Constraints:

# 1 <= s.length, t.length <= 10^5
# 0 <= k <= 10^9
# s, t contain only lowercase English letters.



# this does not work 
# class Solution:
#     def canConvertString(self, s: str, t: str, k: int) -> bool:
#         if len(s)!=len(t):
#             return False

#         remove_memo = {}
#         for i in range(len(t)):
#             sidx = ord(s[i])-ord('a')
#             tidx = ord(t[i])-ord('a')
#             diff = min(abs(tidx-sidx),abs(25-tidx+sidx))
#             # diff = min(abs((ord(s[i])-ord('a'))-(ord(t[i])-ord('a'))),(abs(ord(s[i])-ord('a')-ord('z')+1+(ord(t[i])-ord('a')))))
#             # print(diff)
#             if diff == 0:
#                 continue
#             if diff not in remove_memo:
#                 remove_memo[diff]=1
#             else:
#                 remove_memo[diff]+=1
#         # print(remove_memo)
#         for j in range(1,k+1):
#             if j in remove_memo:
#                 remove_memo[j]-=1
#                 if remove_memo[j]<=0:
#                     del remove_memo[j]
#                 else:
#                     count = remove_memo[j]
#                     del remove_memo[j]
#                     remove_memo[j+26]=count
        
#         return len(remove_memo)==0



# This works !

class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s)!=len(t):
            return False

        remove_memo = {}
        for i in range(len(t)):
            sidx = ord(s[i])
            tidx = ord(t[i])
            # it does not become negative because I did % (-1%26 = 25)
            diff = (tidx-sidx) % 26

            if diff == 0:
                continue
            if diff not in remove_memo:
                remove_memo[diff]=1
            else:
                remove_memo[diff]+=1
        
        num_repeated = k // 26
        keys = list(remove_memo.keys())
        # print("before: {}".format(remove_memo))
        for key in keys:
            remove_memo[key] -= num_repeated
            if remove_memo[key] <= 0:
                del remove_memo[key]
        # print("after reducing by {}: {}".format(num_repeated, remove_memo))
    
        for j in range(1, (k % 26) + 1):
            # print("checking {}".format(j))
            if j in remove_memo:
                remove_memo[j]-=1
                if remove_memo[j]<=0:
                    del remove_memo[j]
        # print("after final step: {}".format(remove_memo))

        return len(remove_memo)==0
