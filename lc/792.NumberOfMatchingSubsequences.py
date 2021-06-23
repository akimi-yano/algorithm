# 792. Number of Matching Subsequences
# Medium

# 1785

# 104

# Add to List

# Share
# Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
 

# Example 1:

# Input: s = "abcde", words = ["a","bb","acd","ace"]
# Output: 3
# Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
# Example 2:

# Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# Output: 2
 

# Constraints:

# 1 <= s.length <= 5 * 104
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# s and words[i] consist of only lowercase English letters.


# This solution works:

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def is_word_present(word):
            cur_pos = 0
            for char in word:
                # bisect left looks for an insertion position for the cur_pos
                # if it exists, the idx will be the left side of the existing one(s)
                idx = bisect_left(positions[char], cur_pos)
                if idx > len(positions[char])-1:
                    return False
                # keep moving the index forward
                cur_pos = positions[char][idx]+1
            return True
        
        # use defaultdict to avoid key error for looking for a char that does not exist
        positions = defaultdict(list)
        # store the idx positions
        for i, char in enumerate(s):
            positions[char].append(i)
        # count the number of word that exists by returning true or false
        return sum(is_word_present(word) for word in words)