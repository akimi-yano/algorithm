# 890. Find and Replace Pattern
# Medium

# 1201

# 97

# Add to List

# Share
# Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 

# Example 1:

# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]
# Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
# "ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
# Example 2:

# Input: words = ["a","b","c"], pattern = "a"
# Output: ["a","b","c"]
 

# Constraints:

# 1 <= pattern.length <= 20
# 1 <= words.length <= 50
# words[i].length == pattern.length
# pattern and words[i] are lowercase English letters.

# This solution works:

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for word in words:
            w_p = {}
            p_w = {}
            for i in range(len(word)):
                if word[i] not in w_p:
                    w_p[word[i]] = pattern[i]
                else:
                    if w_p[word[i]] != pattern[i]:
                        break
                if pattern[i] not in p_w:
                    p_w[pattern[i]] = word[i]
                else:
                    if p_w[pattern[i]] != word[i]:
                        break
            else:
                ans.append(word)
        return ans    
            

# This solution works - another solution:

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        plist = []
        pmap = {}
        cur = 0
        for letter in pattern:
            if letter not in pmap:
                pmap[letter] = cur
                cur +=1 
            plist.append(pmap[letter])
        
        ans = []
        for word in words:
            wlist = []
            wmap = {}
            cur = 0
            for letter in word:
                if letter not in wmap:
                    wmap[letter] = cur
                    cur +=1
                wlist.append(wmap[letter])
                if wlist[len(wlist)-1] != plist[len(wlist) - 1]:
                    break
            else:
                ans.append(word)
    
        return ans