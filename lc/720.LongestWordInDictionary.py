# 720. Longest Word in Dictionary
# Easy

# 684

# 795

# Add to List

# Share
# Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

# If there is no answer, return the empty string.
# Example 1:
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
# Note:

# All the strings in the input will only contain lowercase letters.
# The length of words will be in the range [1, 1000].
# The length of words[i] will be in the range [1, 30].



# This approach does not work :
# class Node:
#     def __init__(self):
#         self.next = {}
#         self.is_word = False
        
# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         self.root = Node()
#         cur = self.root
#         for word in words:
#             for char in word:
#                 if char not in cur.next:
#                     cur.next[char] = Node()
#                 else:
#                     cur = cur.next[char]
#             cur.is_word = True
    
# This approach does not work:

# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         words.sort()

#         prev = words[0]
#         length = 1
#         for i in range(1,len(words)):
#             if words[i][:-1] == prev:
#                 length +=1
#                 prev = words[i]
        
#         return prev




# This approach works !!!! Trie 

class Node:
    def __init__(self):
        self.next = {}
        self.is_word = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # make trie
        self.root = Node()
        for word in words:
            cur = self.root
            for char in word:
                if char not in cur.next:
                    cur.next[char] = Node()
                cur = cur.next[char]
            cur.is_word = True
        
        # make helper to dfs traverse
        # print(self.root.next)
        if not self.root:
            return ''
        self.best = ''
        
        def helper(cur_node, word_so_far):
            if len(word_so_far) > len(self.best):
                self.best = word_so_far
            elif len(word_so_far) == len(self.best) and word_so_far < self.best:
                self.best = word_so_far
            for next_char, next_node in cur_node.next.items():
                if next_node.is_word:
                    helper(next_node, word_so_far + next_char)

        helper(self.root, '')
        return self.best
    
# This approach works !!! Union Find !!!!
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = {word: word for word in words}
        def find(a):
            if a != root[a]:
                root[a] = find(root[a])
            return root[a]

        def union(a, b):
            ar, br = find(a), find(b)
            root[ar] = br
            root[a] = find(a)
        
        wordset = set(words)
        for word in wordset:
            if word[:-1] in wordset:
                union(word, word[:-1])
        for word in words:
            find(word)
        best = ''
        for word, wordroot in root.items():
            if len(wordroot) == 1:
                if len(best) < len(word):
                    best = word
                elif len(best) == len(word) and best > word:
                    best = word
        # print(root)
        return best
    
    
# Contributed to the leetcode community !
'''
[Python] Union Find w/ Explanation
0
codingrobot2020's avatar
codingrobot2020
0
a few seconds ago

Idea: Union Find to group words and use the shortest word as the root.

Steps:

Make a set of the words, wordset
For each word, look in the wordset for a word with the last character removed
If it exists, do a union(), using the shorter word as the root
Walk through the all the node->root pairs, and consider all words where the root is 1 character long
Choose the longest word, using the lexographical order to break ties
'''
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = {word: word for word in words}

        def find(a):
            if a != root[a]:
                root[a] = find(root[a])
            return root[a]

        def union(a, b):
            ar, br = find(a), find(b)
            root[ar] = br
            root[a] = find(a)
        
        wordset = set(words)
        for word in wordset:
            if word[:-1] in wordset:
                union(word, word[:-1])
        for word in words:
            find(word)

        best = ''
        for word, wordroot in root.items():
            if len(wordroot) == 1:
                if len(best) < len(word):
                    best = word
                elif len(best) == len(word) and best > word:
                    best = word

        return best