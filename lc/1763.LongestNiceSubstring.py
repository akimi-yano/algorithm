# 1763. Longest Nice Substring
# Easy

# 39

# 66

# Add to List

# Share
# A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

# Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

# Example 1:

# Input: s = "YazaAay"
# Output: "aAa"
# Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
# "aAa" is the longest nice substring.
# Example 2:

# Input: s = "Bb"
# Output: "Bb"
# Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
# Example 3:

# Input: s = "c"
# Output: ""
# Explanation: There are no nice substrings.
# Example 4:

# Input: s = "dDzeE"
# Output: "dD"
# Explanation: Both "dD" and "eE" are the longest nice substrings.
# As there are multiple longest nice substrings, return "dD" since it occurs earlier.
 

# Constraints:

# 1 <= s.length <= 100
# s consists of uppercase and lowercase English letters.

# This solution works:

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        alpha1 = {}
        alpha2 = {}
        for i in range(26):
            alpha1[chr(ord('a')+i)] = chr(ord('A')+i)
            alpha2[chr(ord('A')+i)] = chr(ord('a')+i)
        bestlength = 0
        best = ""
        for start in range(len(s)):
            for end in range(start+1, len(s)+1):
                seen = set(s[start:end])
                for cur in range(start, end):
                    if s[cur] in alpha1:
                        if alpha1[s[cur]] not in seen:
                            break
                    else:
                        if alpha2[s[cur]] not in seen:
                            break
                else:
                    maybe_ans = s[start:end]
                    if len(maybe_ans) > bestlength:
                        best = maybe_ans
                        bestlength = len(maybe_ans)
        return best