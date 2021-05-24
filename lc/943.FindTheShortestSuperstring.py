# 943. Find the Shortest Superstring
# Hard

# 661

# 101

# Add to List

# Share
# Given an array of strings words, return the smallest string that contains each string in words as a substring. If there are multiple valid strings of the smallest length, return any of them.

# You may assume that no string in words is a substring of another string in words.

 

# Example 1:

# Input: words = ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be accepted.
# Example 2:

# Input: words = ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"
 

# Constraints:

# 1 <= words.length <= 12
# 1 <= words[i].length <= 20
# words[i] consists of lowercase English letters.
# All the strings of words are unique.

# This solution works:

class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:
        '''
        used_words = [1, 0, 1, 1, 0, ..., 1]
        4,096 < 10,000 == 10^4
        
        prev_word
        12
        '''
        N = len(words)
        overlaps = [[0] * N for _ in range(N)]
        # overlaps[0][1] = 1
        for w1 in range(N):
            for w2 in range(N):
                if w1 == w2:
                    continue
                word1 = words[w1]
                word2 = words[w2]
                max_overlap = min(len(word1), len(word2))
                
                best = 0
                for overlap in range(max_overlap, 0, -1):
                    # word1 = "boba"
                    # word2 = "bat"
                    # overlap = 2
                    # if overlap = 2 -> last 2 chars in "boba" == first 2 chars in "bat"
                    # looping from 0->1
                    # @i=0 : "boba"[-2+0] -> "boba"[-2] == "bat"[0]
                    # @i=1 : "boba"[-2+1] -> "boba"[-1] == "bat"[1]
                    for i in range(overlap):
                        if word1[-overlap + i] != word2[i]:
                            break
                    else:
                        best = overlap
                        break
                overlaps[w1][w2] = best
        
        @lru_cache(None)
        def helper(used_words, prev_i):
            if all(used_words):
                return ''
            
            best = None
            for i, used in enumerate(used_words):
                # if used == 1, the word has been used.
                if used:
                    continue

                word = words[i]
                new_used_words = list(used_words)
                new_used_words[i] = 1
                
                cur = word
                if prev_i >= 0:
                    cur = word[overlaps[prev_i][i]:]
                    
                cur += helper(tuple(new_used_words), i)
                if best is None or len(cur) < len(best):
                    best = cur
            return best
        
        return helper(tuple(0 for _ in words), -1)
