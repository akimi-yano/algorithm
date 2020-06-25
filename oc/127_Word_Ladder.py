# 127 Word Ladder
# Prompt
# Given a begin and end word, along with a list of words, return the
#  length of the shortest transformation sequence

# Examples:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log","cog"]

# result = 5

# Reason:
# The shortest transformation sequence from "hit" to "cog" is:

# "hit" -> "hot" -> "dot" -> "dog" -> "cog"

# Because this sequence contains 5 elements, we return 5
#                    -------------
#                    |           |
# hit - hot - dot - dog - log - cog
#         |    |           |
#         |    |           |
#         lot --------------
        
#        a= "abc"
#        b= "defg"
#        zip(a,b) = [('a','d'), ('b','e')] 
       
#                    i                
#       a= ["hot", "hit", "cold", "hello"]
      
#       # dic = obj
#       enumerate(a) = (0, "hot") -- (1, "hit")
        
# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         adjlist = defaultdict(set)
#         for w in wordList:
#             if len(w) == len(beginWord) and sum(a != b for a, b in zip(beginWord, w)) == 1:
#                 adjlist[beginWord].add(w)
#                 adjlist[w].add(beginWord) 
#         for i, w1 in enumerate(wordList):
#             for j in range(i+1, len(wordList)):
#                 w2 = wordList[j]
#                 if len(w1) == len(w2) and sum(a != b for a, b in zip(w1, w2)) == 1:
#                     adjlist[w1].add(w2)
#                     adjlist[w2].add(w1)
#         qu = deque([beginWord])
#         qulen = 1
#         seen = set()
#         seen.add(beginWord)
#         distance = 0
#         while qu:
#             distance += 1
#             qulen = len(qu)
#             for _ in range(qulen):
#                 node = qu.popleft()
#                 if node == endWord: 
#                     return distance
#                 for nei in adjlist[node]:
#                     if nei not in seen:
#                         qu.append(nei)
#                         seen.add(nei)
#         return 0











