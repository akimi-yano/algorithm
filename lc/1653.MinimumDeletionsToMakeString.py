# 1653. Minimum Deletions to Make String Balanced
# Medium

# 107

# 1

# Add to List

# Share
# You are given a string s consisting only of characters 'a' and 'b'​​​​.

# You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

# Return the minimum number of deletions needed to make s balanced.

 

# Example 1:

# Input: s = "aababbab"
# Output: 2
# Explanation: You can either:
# Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
# Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").
# Example 2:

# Input: s = "bbaaaaabb"
# Output: 2
# Explanation: The only solution is to delete the first two characters.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is 'a' or 'b'​​.


# These approaches do not work 
'''
        bad case
        ba
        
        good case
        aa
        ab
        bb
        
        "baababbaabbaaabaabbabbbabaaaaaabaabab abaaababbb" ->18
        fa 1
        ac 1
        fb 0
        bc 0
        t 2
'''
        # founda = False
        # foundb = False
        # acount = 0
        # bcount = 0
        # total = 0
        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == 'a':
        #         if foundb:
        #             total += min(acount, bcount)
        #             foundb = False
        #             acount = 0
        #             bcount = 0
        #         acount += 1
        #         founda = True
        #     else:
        #         if founda:
        #             foundb = True
        #             bcount += 1
        # if foundb:
        #     total += min(acount, bcount)
        # return total
        
        #     def helper(prev, i):
        #     if i > len(s)-1:
        #         return float('inf')
        #     min_rm = float('inf')
        #     if prev == 'a'  and s[i] == 'b'
        #         min_rm = min(min_rm, helper())
        
        # return helper("b", len(s)-1)
        
        
        # acount = 0
        # bcount = 0
        # total = 0
        # for i in range(len(s)):
        #     if s[i] == 'a':
        #         if bcount:
        #             acount += 1        
        #     else:
        #         if bcount and acount:
        #             total += min(acount, bcount)
        #             acount = bcount =0 
        #         bcount += 1
        # if acount and bcount:
        #     total += min(acount, bcount)
                
        # return total
        
        
# This approach does not work 
# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         def helper(prev, i):
#             if i > len(s)-1:
#                 return 0
#             min_rm = 0
#             if prev == 'b'  and s[i] == 'a':
#                 min_rm += min(1+helper('a',i+1) + self.arr_b[i], 1+helper('b',i+1) + self.arr_a[i])
#             else:
#                 min_rm += helper(s[i],i+1)

#             return min_rm
        
#         arr_a = []
#         arr_b = []
#         acount = 0
#         bcount = 0
#         for i in range(len(s)):
#             if s[i] == 'b':
#                 acount = 0
#                 bcount += 1
#             else:
#                 acount += 1
#                 bcount = 0
#             arr_a.append(acount)
#             arr_b.append(bcount)
#         self.arr_a = arr_a
#         self.arr_b = arr_b
#         return helper("a", 0)
                    
'''
its too late to remove when prev is B and cur is A
think if we should remove cur when prev is A and  cur is B
'''

# This approach TLE 

# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         memo = {}
#         def helper(prev, i):
#             key = (prev, i)
#             if key in memo:
#                 return memo[key]
            
#             min_rm = 0
#             if i > len(s)-1:
#                 pass
#             elif prev == 'a'  and s[i] == 'b':
#                 min_rm += min(1+ helper('a', i+1), helper('b', i+1))
#             elif prev == 'b' and s[i] == 'a':
#                 min_rm += 1 + helper(prev, i+1)
#             else:
#                 min_rm += helper(prev, i+1)
#             memo[key] = min_rm
#             return min_rm
        
        
#         return helper("a", 0)
                    

# This approach does not work: TLED

# class Solution:
#     def minimumDeletions(self, s: str) -> int:
#         self.memo = {}
#         def helper(prev, i):
#             key = (prev, i)
#             if key in self.memo:
#                 return self.memo[key]
            
#             min_rm = 0
#             if i > len(s)-1:
#                 pass
#             elif prev == 'a'  and s[i] == 'b':
#                 min_rm += min(1+ helper('a', i+1), helper('b', i+1))
#             elif prev == 'b' and s[i] == 'a':
#                 min_rm += 1 + helper(prev, i+1)
#             else:
#                 min_rm += helper(prev, i+1)
#             self.memo[key] = min_rm
#             return min_rm
        
        
#         return helper("a", 0)
                    


# This solution works !!!
'''
partition the string and for each border/ partition, calcurate how many As and Bs you need to delete and get the min
user a counter dict and add and subtract as you see an element
'''

from collections import Counter
class Solution:
    def minimumDeletions(self, s: str) -> int:
        counts = Counter(s)
        a_left = b_left = 0
        a_right = counts['a']
        b_right = counts['b']
        
        # initial case is deleting all As
        best = a_right
        for x in s:
            if x == 'a':
                a_right -= 1
                a_left += 1
            else:
                b_right -= 1
                b_left += 1
            best = min(best, b_left + a_right)
        return best