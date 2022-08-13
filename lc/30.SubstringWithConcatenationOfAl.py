# 30. Substring with Concatenation of All Words
# Hard

# 2505

# 2006

# Add to List

# Share
# You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

# You can return the answer in any order.

 

# Example 1:

# Input: s = "barfoothefoobarman", words = ["foo","bar"]
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
# Example 2:

# Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
# Output: []
# Example 3:

# Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
# Output: [6,9,12]
 

# Constraints:

# 1 <= s.length <= 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 30
# s and words[i] consist of lowercase English letters.


# This solution works:


class Solution:
    def findSubstring(self, s, words):
        if not words: return []
        k = len(words[0])
        res = []
        for left in range(k):
            d = collections.Counter(words)
            for right in range(left + k, len(s) + 1, k):
                word = s[right - k: right]
                d[word] -= 1
                while d[word] < 0:
                    d[s[left:left + k]] += 1
                    left += k
                if left + k * len(words) == right:
                    res.append(left)
        return res

