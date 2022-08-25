# 383. Ransom Note
# Easy

# 2510

# 350

# Add to List

# Share
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

 

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true
 

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


# This solution works:


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        goals = Counter(ransomNote)
        options = Counter(magazine)
        for char, num in goals.items():
            if char not in options or num > options[char]:
                return False
        return True 