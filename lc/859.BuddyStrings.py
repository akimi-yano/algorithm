# 859. Buddy Strings
# Easy

# 727

# 494

# Add to List

# Share
# Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

# Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

# Example 1:

# Input: A = "ab", B = "ba"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.
# Example 2:

# Input: A = "ab", B = "ab"
# Output: false
# Explanation: The only letters you can swap are A[0] = 'a' and A[1] = 'b', which results in "ba" != B.
# Example 3:

# Input: A = "aa", B = "aa"
# Output: true
# Explanation: You can swap A[0] = 'a' and A[1] = 'a' to get "aa", which is equal to B.
# Example 4:

# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
# Example 5:

# Input: A = "", B = "aa"
# Output: false

# Constraints:

# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist of lowercase letters.


# This solution works !:
'''
just finding two different indexes that have different values
if the indexes are the same, they dont have any pair of indexes whose values are different 
-> check if there are any duplicated characters that we can just simply swap
'''

class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if not A and not B:
            return False
        if len(A) != len(B):
            return False
        A = list(A)
        B = list(B)
        left = 0
        right = len(A)-1
        while left < right:
            if A[left] == B[left]:
                left += 1
            elif A[right] == B[right]:        
                right -= 1
            else:
                break

        if left == right and len(set(A)) == len(A):
            return False
        
        A[left], A[right] = A[right], A[left]
        
        if A == B:
            return True
        return False
        
            