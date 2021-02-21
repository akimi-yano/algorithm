# 1771. Maximize Palindrome Length From Subsequences
# Hard

# 43

# 2

# Add to List

# Share
# You are given two strings, word1 and word2. You want to construct a string in the following manner:

# Choose some non-empty subsequence subsequence1 from word1.
# Choose some non-empty subsequence subsequence2 from word2.
# Concatenate the subsequences: subsequence1 + subsequence2, to make the string.
# Return the length of the longest palindrome that can be constructed in the described manner. If no palindromes can be constructed, return 0.

# A subsequence of a string s is a string that can be made by deleting some (possibly none) characters from s without changing the order of the remaining characters.

# A palindrome is a string that reads the same forward as well as backward.

 

# Example 1:

# Input: word1 = "cacb", word2 = "cbba"
# Output: 5
# Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba", which is a palindrome.
# Example 2:

# Input: word1 = "ab", word2 = "ab"
# Output: 3
# Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which is a palindrome.
# Example 3:

# Input: word1 = "aa", word2 = "bb"
# Output: 0
# Explanation: You cannot construct a palindrome from the described method, so return 0.
 

# Constraints:

# 1 <= word1.length, word2.length <= 1000
# word1 and word2 consist of lowercase English letters.

# This solution works:

import string
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        '''
        word1 = "cacb", word2 = "cbba"
        "ab"            "cba"         =  "abcba", which is a palindrome
        combine two strings and make word = word1+word2
        word = cacbcbba
        find the same character - left and right and start from there
        for palindrome, the start and end are the same character
        to show all the alphabets - import string and do string.ascii_lowercase
        to find the index of the first occurence of the element in a string, use .find()
        to find the index of the last occurence of the element in a string, use .rfind()
        if the index is -1, it means we could not find the character
        '''
        @lru_cache(None)
        def helper(left, right):
            nonlocal word
            if left == right:
                return 1
            if left > right:
                return 0
            if word[left] == word[right]:
                return 2 + helper(left+1, right-1)
            return max(helper(left, right-1), helper(left+1, right))
        
        word = word1 + word2
        best_length = 0
        for char in string.ascii_lowercase:
            start = word1.find(char)
            end = word2.rfind(char)
            if start != -1 and end != -1:
                best_length = max(best_length, helper(start, len(word1)+end))
        return best_length