# 1048. Longest String Chain
# Medium

# 1865

# 109

# Add to List

# Share
# Given a list of words, each word consists of English lowercase letters.

# Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

# Return the longest possible length of a word chain with words chosen from the given list of words.

 

# Example 1:

# Input: words = ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: One of the longest word chain is "a","ba","bda","bdca".
# Example 2:

# Input: words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
# Output: 5
 

# Constraints:

# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.

# This solution works:

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        length = {}
        for word in words:
            if len(word) not in length:
                length[len(word)] = []
            length[len(word)].append(word)
        
        @lru_cache(None)
        def helper(prev):
            if (len(prev) + 1) not in length:
                return 0
            MAX = 0
            for maybe_next in length[len(prev) + 1]:
                for i in range(len(maybe_next)):
                    if maybe_next[:i] + maybe_next[i+1:] == prev:
                        MAX = max(MAX, 1 + helper(maybe_next))
            return MAX
        
        MAX = 0
        for word in words:
            MAX = max(MAX, 1 + helper(word))
        return MAX