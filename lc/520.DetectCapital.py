# 520. Detect Capital
# Easy

# 1163

# 333

# Add to List

# Share
# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.


# This solution works:


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        low_word = word.lower()
        upper_word = word.upper()
        first_upper_word = low_word[0].upper() + low_word[1:]
        correct = [low_word, upper_word, first_upper_word]
        return any(word == choice for choice in correct)