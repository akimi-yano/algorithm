# 126. Word Ladder II
# Hard

# 2852

# 310

# Add to List

# Share
# A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

# Every adjacent pair of words differs by a single letter.
# Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
# sk == endWord
# Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

 

# Example 1:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# Explanation: There are 2 shortest transformation sequences:
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
# Example 2:

# Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

# Constraints:

# 1 <= beginWord.length <= 5
# endWord.length == beginWord.length
# 1 <= wordList.length <= 1000
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


# This solution works:


# The idea of this problem is to run bfs, where one step is changing some letter of word. For me easier to separate problem to two parts:

# Create graph of connections G.
# Run bfs on this graph with collecting all possible solutions.
# Now, let us consider steps in more details.

# To create graph of connections for each word, for example hit, create patterns *it, h*t, hi*. Then iterate over patterns and connect words in our defaultdict G.

# We need to run bfs, but we also need to give as answer all possible solutions, so, we need to modify our algorithm a bit. We keep two dictionaries: deps for depths of each word and paths to keep all possible paths. When we extract element from queue and look at its neighbours, we need to add new element to queue if deps[neib] == -1. Also we need to update paths[neib] if deps[neib] == -1 or deps[neib] == deps[w] +, that is to deal with all ways of optimal length.

# Complexity
# We need O(nk^2) time to create all possible patterns: for each of n words we have k patterns with length k. Then we will have no more than O(n*k*26) possible connections for all pairs of words, each of which has length k, so to create G we need O(nk^2*26) time. In practice thought this number is smaller, because graph can not have this number of connections. For the last part with bfs we have complexity O(nk^2*26) again, because this is the number of edges in our graph + A, where A is number of found solutions, which can be exponential. So, time complexity is O(nk^2*26 + A), space is the same.

class Solution:
    def findLadders(self, begW, endW, wordList):
        wordList += [begW]
        n, k = len(wordList), len(wordList[0])
        patterns = defaultdict(set)
        for word in wordList:
            for ind in range(0, k):
                tmp = word[0:ind] + "*" + word[ind+1:]
                patterns[tmp].add(word)
                
        G = defaultdict(set)
        for elem in patterns.values():
            for x, y in permutations(elem, 2):
                G[x].add(y)
                
        deps = {w: -1 for w in wordList}
        deps[begW] = 0
        paths = defaultdict(list)
        paths[begW] = [[begW]]
        queue = deque([begW])

        while queue:
            w = queue.popleft()
            if w == endW: return paths[w]
            for neib in G[w]:
                if deps[neib] == -1 or deps[neib] == deps[w] + 1:
                    if deps[neib] == -1:
                        queue.append(neib)
                        deps[neib] = deps[w] + 1
                    for elem in paths[w]:
                        paths[neib].append(elem + [neib])