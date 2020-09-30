# 680. Valid Palindrome II
# Easy

# 1936

# 124

# Add to List

# Share
# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.



# This solution does not work 
# class Solution:
#     def validPalindrome(self, s: str) -> bool:
#         '''
#         start from middle and middle -1
#         recursion and try all the cases
#         '''
        
#         def helper(mid1, mid2, flipped, even):
#             if mid1 < 0 or mid2 > len(s)-1:
#                 return True
#             ans = False
#             if s[mid1] == s[mid2]:
#                 ans |= helper(mid1-1,mid2+1,flipped,even)
#             else:
#                 if not flipped:
#                     ans |= helper(mid1,mid2+1,True,even)
#                     ans |= helper(mid1-1,mid2,True,even)
# #                     if even:
# #                         ans |= helper(mid1-1,mid2+1,True,even)
#                 else: 
#                     return False
#             return ans

#         if len(s)%2 == 0:
#             return helper(len(s)//2-1, len(s)//2, False, True)
#         else:
#             return helper(len(s)//2, len(s)//2, False, False)



# THIS SOLUTION WORKS !
'''
step 1: find the indexes whose values are not matching 
step 2: move start scenario
step 3: move end scenario
if step 1 - 3 does not return True, return False
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
    
        # step 1: find the indexes whose values are not matching 
        while start <= end and s[start] == s[end]:
            start += 1
            end -=1
        # it went all the way to the end, then return True
        if start > end:
                return True
        
        # save the start and end so that I can check 2 cases: move start and move end
        temp_start = start
        temp_end = end
        
        
        # step 2: move start
        start = temp_start + 1
        end = temp_end
        
        while start <= end and s[start] == s[end]:
            start += 1
            end -=1

        if start > end:
            return True
        
        # step 3: move end
        start = temp_start
        end = temp_end -1
        while start <= end and s[start] == s[end]:
            start += 1
            end -=1

        if start > end:
            return True
            
        return False
    
    
# This solution works  !!! - code modularization

class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def helper(start, end):
            while start <= end and s[start] == s[end]:
                start += 1
                end -=1
            return  start, end
        
        # step 1: find the indexes whose values are not matching 
        start, end = helper(0, len(s)-1)
        # it went all the way to the end, then return True
        if start > end:
                return True
        
        # save the start and end so that I can check 2 cases: move start and move end
        temp_start = start
        temp_end = end
        
        # step 2: move start
        start, end = helper(temp_start + 1, temp_end)
        if start > end:
            return True
        
        # step 3: move end
        start, end = helper(temp_start, temp_end -1)
        if start > end:
            return True
            
        return False