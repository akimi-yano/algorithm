# 1781. Sum of Beauty of All Substrings
# Medium

# 41

# 31

# Add to List

# Share
# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.

 

# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.
# Example 2:

# Input: s = "aabcbaa"
# Output: 17
 

# Constraints:

# 1 <= s.length <= 500
# s consists of only lowercase English letters.


# This solution works - brute force works:

from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for start in range(len(s)):
            counts = Counter([])
            for end in range(start, len(s)):
                counts[s[end]] += 1
                if len(counts) > 1:
                    total += max(counts.values()) - min(counts.values())
        return total
        '''
        "aabcb"
        
        "aab",
         "aabc",
         "aabcb",
          "abcb",
           "bcb"
        
        
        "aabcbaa"
        "aab" 1
        "aabc"1
        "aabcb"1
        "aabcba"2
        "aabcbaa"3
         "abcb"1
         "abcba"1
         "abcbaa"2
          "bcb"1
          "bcba"1
          "bcbaa"1
           "cbaa"1
            "baa"1
        
        
        '''