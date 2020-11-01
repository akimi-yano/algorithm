# 1641. Count Sorted Vowel Strings
# Medium

# 48

# 2

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


# This solution works !!

class Solution:
    def countVowelStrings(self, n: int) -> int:
        choices = ["a","e","i","o","u"]
    
        memo = {}
        def helper(prev, i, n):
            key = (prev, i, n)
            if key in memo:
                return memo[key]
            ways = 0
            if n == 0:
                ways = 1
            elif i > len(choices)-1:
                pass
            else:
                if prev <= choices[i]:
                    ways += helper(choices[i], i, n-1)
                ways += helper(prev, i+1, n)
            memo[key] = ways
            return ways
            
        return helper("a", 0, n)
        