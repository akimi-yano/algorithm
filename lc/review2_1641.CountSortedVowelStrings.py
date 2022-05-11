# 1641. Count Sorted Vowel Strings
# Medium

# 1816

# 41

# Add to List

# Share
# Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

# A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 

# Example 1:

# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
# Example 2:

# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.
# Example 3:

# Input: n = 33
# Output: 66045
 

# Constraints:

# 1 <= n <= 50 


# This solution works:


class Solution:
    def countVowelStrings(self, n: int) -> int:
        @lru_cache(None)
        def helper(i, remaining):
            if not remaining:
                return 1
            if not i:
                return 0
            return helper(i, remaining-1) + helper(i-1, remaining) #use vs not use
            
        return helper(5, n)