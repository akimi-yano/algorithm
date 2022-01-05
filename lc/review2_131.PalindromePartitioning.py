# 131. Palindrome Partitioning
# Medium

# 5042

# 154

# Add to List

# Share
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# A palindrome string is a string that reads the same backward as forward.

 

# Example 1:

# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:

# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.


# This solution works:

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def helper(substr):
            if not substr:
                return [[]]
            ans = []
            for end in range(len(substr)):
                char = substr[:end+1]
                if self.is_palindrome(char):
                    ans.extend([[char] + arr for arr in helper(substr[end+1:])])
            return ans
        return helper(s)
    
    def is_palindrome(self, char):
        left = 0
        right = len(char)-1
        while left < right:
            if char[left] != char[right]:
                return False
            left += 1
            right -= 1
        return True
