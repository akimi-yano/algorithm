# 916. Word Subsets
# Medium

# 646

# 100

# Add to List

# Share
# We are given two arrays A and B of words.  Each word is a string of lowercase letters.

# Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example, "wrr" is a subset of "warrior", but is not a subset of "world".

# Now say a word a from A is universal if for every b in B, b is a subset of a. 

# Return a list of all universal words in A.  You can return the words in any order.

 

# Example 1:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]
# Example 2:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["l","e"]
# Output: ["apple","google","leetcode"]
# Example 3:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","oo"]
# Output: ["facebook","google"]
# Example 4:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["lo","eo"]
# Output: ["google","leetcode"]
# Example 5:

# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
# Output: ["facebook","leetcode"]
 

# Note:

# 1 <= A.length, B.length <= 10000
# 1 <= A[i].length, B[i].length <= 10
# A[i] and B[i] consist only of lowercase letters.
# All words in A[i] are unique: there isn't i != j with A[i] == A[j].





# This approach does not work:

# class Solution:
#     def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
#         '''
#         arr A 10 ^ 4
#         char in arr A 10
#         Total: 10 ^ 5
        
#         arr B 10 ^ 4
#         char in arr B 10
#         Total: 10 ^ 5
        
#         If we have everything of B in A then return those
        
#         Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["ec","oc","ceo"]
#         a:2 
#         m:1
#         z:1
#         o:1
#         n:1
        
#         e:1
#         c:1
        
        
#         Output: ["facebook","leetcode"]
#         '''
#         counts = {}
#         for word in A:
#             counts[word] = {}
#             for letter in word:
#                 if letter not in counts[word]:
#                     counts[word][letter] = 0
#                 counts[word][letter] += 1
        
#         ans = []
#         for word, counts in counts.items():
#             found = False
#             for b_word in B:
#                 a_counts = dict(counts)
#                 for char in b_word:
#                     if char not in a_counts:
#                         found = False
#                         break
#                     else:
#                         a_counts[char] -= 1
#                         if a_counts[char] < 1:
#                             del a_counts[char]
#                 else:
#                     found = True
#                 if not found:
#                     break
#             else:
#                 ans.append(word)

#         return ans

                

# This solution works:

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:

        counts = {}
        for word in A:
            counts[word] = {}
            for letter in word:
                if letter not in counts[word]:
                    counts[word][letter] = 0
                counts[word][letter] += 1
        
        types = {}
        for word in B:
            must_haves = Counter()
            for char in word:
                must_haves[char] += 1
            for k, v in must_haves.items():
                if k in types:
                    types[k] = max(types[k], v)
                else:
                    types[k] = v

        ans = []
        for word, a_counts in counts.items():
            for char, num in types.items():
                if char not in a_counts or a_counts[char] < num:
                    break
                else:
                    a_counts[char] -= num
                    if a_counts[char] < 1:
                        del a_counts[char]              
            else:
                ans.append(word)
        return ans

                
                
# This solution works - optimization:
from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counts = Counter()
        for b in B:
            for letter, count in Counter(b).items():
                counts[letter] = max(counts[letter], count)
        ans = []
        for a in A:
            ans.append(a)
            ac = Counter(a)
            for letter, count in counts.items():
                if ac[letter] < count:
                    ans.pop()
                    break
        return ans