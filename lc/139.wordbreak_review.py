# 139. Word Break
# Medium

# 5086

# 253

# Add to List

# Share
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false


# This solution works ! recursion + memorization

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def helper(s, words):
            if s in memo:
                return memo[s]
            
            if len(s) < 1:
                return True
            
            ans = False    
            for word in words:
                if word == s[:len(word)]:
                    ans |= helper(s[len(word):], words)
            
            memo[s] = ans
            
            return ans
        return helper(s, wordDict)


# This solution also works ! trie + lru_cache

class Node:
    def __init__(self):
        self.next = {}
        self.is_word = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.root = Node()
        
        for word in wordDict:
            cur = self.root
            for char in word:
                if char not in cur.next:
                    cur.next[char] = Node()
                cur = cur.next[char]
            cur.is_word = True
           
        # self.memo = {}
        return self.search(s)
    
    @lru_cache(None)
    def search(self, s):
        # if s in self.memo:
        #     return self.memo[s]
        
        if len(s)<1:
            return True
        
        cur = self.root
        for i, char in enumerate(s):
            if char not in cur.next:
                return False

            if cur.next[char].is_word:
                if self.search(s[i + 1:]):
                    return True
            cur = cur.next[char]
        
        ans = cur.is_word
        # self.memo[s] = ans
        return ans
        