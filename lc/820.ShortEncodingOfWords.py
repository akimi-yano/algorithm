# 820. Short Encoding of Words
# Medium

# 466

# 159

# Add to List

# Share
# A valid encoding of an array of words is any reference string s and array of indices indices such that:

# words.length == indices.length
# The reference string s ends with the '#' character.
# For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
# Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

 

# Example 1:

# Input: words = ["time", "me", "bell"]
# Output: 10
# Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
# words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
# words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
# words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"
# Example 2:

# Input: words = ["t"]
# Output: 2
# Explanation: A valid encoding would be s = "t#" and indices = [0].

 

# Constraints:

# 1 <= words.length <= 2000
# 1 <= words[i].length <= 7
# words[i] consists of only lowercase letters.


# This approach does not work:

# class Solution:
#     def minimumLengthEncoding(self, words: List[str]) -> int:
#         def helper(i, cur, seen):
            
#             nonlocal minlength
#             if not seen:
#                 minlength = min(minlength, len(cur))
#                 return True
            
#             if i > len(words)-1 or i not in seen:
#                 return False
            
#             target = words[i] 
#             for idx in set(seen):
#                 if idx not in seen:
#                     continue
#                 seen.remove(idx)
#                 temp = words[idx]
#                 if target[len(target)-len(temp):] == temp:     
#                     if helper(i+1, cur+target[len(target)-len(temp):] + "#", seen):
#                         break
#                 seen.add(idx)
#             else:
#                 helper(i+1, cur+target + "#", seen)
            
#             return True
        
#         minlength = float('inf')
#         helper(0, "", set([k for k in range(len(words))]))
#         return minlength

# This solution works:

'''
sort by length (reverse = True)
look from the longest length add add its partials to seen
if its in the seen set we dont add it to answer
at the end we return the sum of (each elem's length + 1)

Time: O(NlogN)
Space: O(N)

'''

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        seen = set()
        words.sort(key = lambda x : len(x), reverse = True)
        ans = []
        
        for word in words:
            if word not in seen:
                ans.append(word)
                for i in range(len(word)):
                    seen.add(word[i:])

        return sum(len(elem)+1 for elem in ans)
                    
                    