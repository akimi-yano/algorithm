# 127. Word Ladder

# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

# Only one letter can be changed at a time.
# Each transformed word must exist in the word list.
# Note:

# Return 0 if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.
# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.






# TLEed and 22 / 43 test cases passed - so this is not the best approach ....
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    
#         # words = set(wordList)
#         words = {}
#         for w in wordList:
#                 words[w]=True
        
#         def helper(word, endWord):    
#             if word == endWord: # word == 'cog'
#                 return 1
#             min_count = float('inf')
#             for i in range(len(word)):
#                 for other_word in words.keys():
                    
#                     if word!= other_word and words[other_word] == True and word[:i]+word[i+1:] == other_word[:i]+other_word[i+1:]:
#                         # print(word,other_word)
#                         if word in words:
#                             words[word] = False
#                         min_count = min(min_count,1+helper(other_word, endWord))
#                         if word in words:
#                             words[word] = True
#             # print(word, min_count)
#             # print(words)
#             return min_count
#         ans = helper(beginWord,endWord) # 'hit'
#         return 0 if ans == float('inf') else ans
    
    
# this works but slow
# from collections import deque

# class Solution:
#     chars = [chr(ord('a')+i) for i in range(26)]
#     def generate_words(self, word):
#         words = set([])
#         for i in range(len(word)):
#             for char in Solution.chars:
#                 new_word = word[:i] + char + word[i+1:]
#                 words.add(new_word)
#         words.remove(word)
#         return words

#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         word_set = set(wordList)

#         queue = deque([(1, beginWord)])
#         while len(queue) > 0:
#             level, word = queue.popleft()
#             if word == endWord:
#                 return level
#             for next_word in self.generate_words(word):
#                 if next_word in word_set:
#                     queue.append((level+1, next_word))
#                     word_set.remove(next_word)
#         return 0






    
# this one works! and fast
from collections import deque
def ladderLength(beginWord, endWord, wordList):
    wordList = set(wordList)
    queue = deque([[beginWord, 1]])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length + 1])
    return 0

print(ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))



# by using all alphabets, 26 which is almost constant ! which is more  efficient than n^2

