# 132. Palindrome Partitioning II
# Hard

# 2404

# 69

# Add to List

# Share
# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s.

 

# Example 1:

# Input: s = "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
# Example 2:

# Input: s = "a"
# Output: 0
# Example 3:

# Input: s = "ab"
# Output: 1
 

# Constraints:

# 1 <= s.length <= 2000
# s consists of lower-case English letters only.


# This solution works:


class Solution:
    def minCut(self, s: str) -> int:
        '''
        1: calculate if each string is a palindrome by storing the beginning and the end
        2: recursion
        '''
        def is_palindrome(mid1, mid2):
            while mid1 >= 0 and mid2 <= len(s)-1 and s[mid1] == s[mid2]:
                if mid1 not in palindromes:
                    palindromes[mid1] = []
                palindromes[mid1].append(mid2)
                mid1 -= 1
                mid2 += 1
            
        palindromes = {}
        # odd palindrome
        for mid in range(len(s)):
            is_palindrome(mid, mid)
        
        # even palindrome
        for mid in range(1, len(s)):
            is_palindrome(mid-1, mid)
        
        @lru_cache(None)
        def helper(start):
            if start > len(s)-1:
                return 0
            min_operations = len(s)
            if start in palindromes:
                for end in palindromes[start]:
                    min_operations = min(min_operations, 1+helper(end+1))
            return min_operations
        return helper(0)-1

