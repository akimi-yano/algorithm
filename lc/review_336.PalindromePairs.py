# 336. Palindrome Pairs
# Hard

# 3186

# 311

# Add to List

# Share
# Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

 

# Example 1:

# Input: words = ["abcd","dcba","lls","s","sssll"]
# Output: [[0,1],[1,0],[3,2],[2,4]]
# Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
# Example 2:

# Input: words = ["bat","tab","cat"]
# Output: [[0,1],[1,0]]
# Explanation: The palindromes are ["battab","tabbat"]
# Example 3:

# Input: words = ["a",""]
# Output: [[0,1],[1,0]]
 

# Constraints:

# 1 <= words.length <= 5000
# 0 <= words[i].length <= 300
# words[i] consists of lower-case English letters.


# This solution works:


class Node:
    def __init__(self):
        self.idx = -1
        self.nexts = {}
    
    def __str__(self):
        return ','.join(k for k in self.nexts)

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[-i-1]:
                    return False
            return True
        
        def helper(sub, node, first_word_idx):
            nonlocal ans
            if node.idx >= 0 and node.idx != first_word_idx:
                if is_palindrome(sub):
                    ans.append([first_word_idx, node.idx])
            for c in node.nexts:
                helper(sub + c, node.nexts[c], first_word_idx)
            

        trie = Node()
        for i, word in enumerate(words):
            cur = trie
            for c in reversed(word):
                if c not in cur.nexts:
                    cur.nexts[c] = Node()
                cur = cur.nexts[c]
            cur.idx = i
        
        ans = []
        for i, word in enumerate(words):
            cur = trie
            for pos in range(len(word)):
                if cur.idx >= 0 and cur.idx != i:
                    sub = word[pos:]
                    if is_palindrome(sub):
                        ans.append([i, cur.idx])
                
                c = word[pos]
                if c not in cur.nexts:
                    cur = None
                    break
                cur = cur.nexts[c]
            
            if cur:
                helper('', cur, i)
        
        return ans
                    