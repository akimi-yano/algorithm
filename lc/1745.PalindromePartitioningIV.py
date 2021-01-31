# 1745. Palindrome Partitioning IV
# Hard

# 48

# 1

# Add to List

# Share
# Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

# A string is said to be palindrome if it the same string when reversed.

 

# Example 1:

# Input: s = "abcbdd"
# Output: true
# Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
# Example 2:

# Input: s = "bcbddxy"
# Output: false
# Explanation: s cannot be split into 3 palindromes.
 

# Constraints:

# 3 <= s.length <= 2000
# s​​​​​​ consists only of lowercase English letters.

# This solution works:

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        self.N = len(s)
        self.palindromes = set([])
        for middle in range(len(s)):
            left = right = middle
            while left >= 0 and right < self.N and s[left] == s[right]:
                self.palindromes.add((left, right))
                left -=1
                right += 1
            left, right = middle, middle + 1
            while left >= 0 and right < self.N and s[left] == s[right]:
                self.palindromes.add((left, right))
                left -=1
                right += 1
        
        for first_end in range(len(s) - 2):
            if (0, first_end) in self.palindromes:
                for second_end in range(first_end+1, len(s)  - 1):
                    if (first_end+1, second_end) in self.palindromes and (second_end + 1, self.N - 1) in self.palindromes:
                        return True
        return False
    
# This solution works - optimization: 

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        self.N = len(s)
        self.palindromes = set([])
        self.first_palindrome_ends = []
        self.third_palindrome_starts = []
        for middle in range(len(s)):
            # odd palindromes
            left = right = middle
            while left >= 0 and right < self.N and s[left] == s[right]:
                self.palindromes.add((left, right))
                if left == 0:
                    self.first_palindrome_ends.append(right)
                if right == self.N - 1:
                    self.third_palindrome_starts.append(left)
                left -=1
                right += 1

            # even palindromes
            left, right = middle, middle + 1
            while left >= 0 and right < self.N and s[left] == s[right]:
                self.palindromes.add((left, right))
                if left == 0:
                    self.first_palindrome_ends.append(right)
                if right == self.N - 1:
                    self.third_palindrome_starts.append(left)
                left -=1
                right += 1
        
        self.first_palindrome_ends.sort()
        self.third_palindrome_starts.sort(reverse=True)
        for first_end in self.first_palindrome_ends:
            for third_start in self.third_palindrome_starts:
                if first_end + 1 >= third_start:
                    break
                middle_start = first_end + 1
                middle_end = third_start - 1
                if (middle_start, middle_end) in self.palindromes:
                    return True
        return False
