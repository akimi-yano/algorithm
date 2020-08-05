# 211. Add and Search Word - Data structure design

# Design a data structure that supports the following two operations:

# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

# Example:

# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.




# This solution does not work - add and the inits are correct !

# from collections import defaultdict
# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(TrieNode)
#         self.is_word = False

# class WordDictionary:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root = TrieNode()

#     def addWord(self, word: str) -> None:
#         """
#         Adds a word into the data structure.
#         """
#         current = self.root
#         for letter in word:
#             current = current.children[letter]
#         current.is_word = True

#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         """
#         def helper(current,i):
#             if i==len(word)-1 and current.is_word ==True:
#                 return True
#             elif i>=len(word)-1:
#                 return False
#             elif word[i] == ".":
#                 for next_node in current.children:
#                     helper(next_node,i+1)
#             else:
#                 if current.children.get(word[i]) is None:
#                     return False
        
#         return helper(self.root,0)
        
        


# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)






# this works

class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False
    
class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isWord:
                self.res = True
            return 
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
            if not node:
                return 
            self.dfs(node, word[1:])