# 567. Permutation in String
# Medium

# 2229

# 78

# Add to List

# Share
# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

 

# Example 1:

# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
 

# Constraints:

# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].


# This solution works:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        
        for start in range(len(s2)):
            temp_s2 = list(sorted(s2[start:start+len(s1)]))
            if temp_s2 == s1:
                return True  
        return False
    

# This solution works - optimization:

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter = {}
        for c in s1:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        for c in s2[:len(s1)]:
            if c not in counter:
                counter[c] = 0
            counter[c] -= 1
            if not counter[c]:
                del counter[c]
        if not counter:
            return True

        for nxt in range(len(s1), len(s2)):
            add_c = s2[nxt]
            del_c = s2[nxt-len(s1)]
            if add_c not in counter:
                counter[add_c] = 0
            if del_c not in counter:
                counter[del_c] = 0
            counter[add_c] -= 1
            counter[del_c] += 1
            if not counter[add_c]:
                del counter[add_c]
            if del_c in counter and not counter[del_c]:
                del counter[del_c]
            if not counter:
                return True
        return False
        