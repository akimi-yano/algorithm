# 126. Word Ladder II
# Hard

# 4066

# 439

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
# 1 <= wordList.length <= 500
# wordList[i].length == beginWord.length
# beginWord, endWord, and wordList[i] consist of lowercase English letters.
# beginWord != endWord
# All the words in wordList are unique.


# This solution works:


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        bfsq = collections.deque()
        res = []
        wordSet =set(wordList)
        parent = collections.defaultdict(list) 
        visited = set()
        mindist = {beginWord: 1}
        visited.add(beginWord)
        bfsq.append((beginWord,1))
        while(bfsq):
            word, dist = bfsq.popleft()
            if word == endWord:
                continue
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    nb = word[:i] + c + word[i+1:]
                    if nb == word or nb not in wordSet:
                        continue
                    if nb not in visited:
                        visited.add(nb)
                        parent[nb].append(word)
                        mindist[nb] = dist+1
                        bfsq.append((nb,dist+1))
                    elif(mindist[nb] == dist+1):
                        parent[nb].append(word)
        if parent.get(endWord, []) == []:
            return []
        def allpaths(path):
            if path == []:
                path.append(endWord)
                for ances in parent[endWord]:
                    allpaths(path + [ances])
            elif path[-1] == beginWord:
                res.append(path)
                return
            else:
                for ances in parent[path[-1]]:
                    allpaths(path + [ances])

        path = []
        allpaths(path)
        for ele in res:
            ele.reverse()
        return res