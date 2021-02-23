# 524. Longest Word in Dictionary through Deleting
# Medium

# 867

# 282

# Add to List

# Share
# Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

# Example 1:
# Input:
# s = "abpcplea", d = ["ale","apple","monkey","plea"]

# Output: 
# "apple"
# Example 2:
# Input:
# s = "abpcplea", d = ["a","b","c"]

# Output: 
# "a"
# Note:
# All the strings in the input will only contain lower-case letters.
# The size of the dictionary won't exceed 1,000.
# The length of all the strings in the input won't exceed 1,000.


# This solution works:

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest = 0
        ans = ""
        for word in d:
            idx1 = idx2 = 0
            while idx1 < len(word) and idx2 < len(s):
                if word[idx1] == s[idx2]:
                    idx1 +=1
                    idx2 +=1
                else:
                    idx2+=1
            if idx1 >= len(word):
                if longest < len(word):
                    longest = len(word)
                    ans = word
                elif longest == len(word):
                    longest = len(word)
                    if not ans or ans > word:
                        ans = word
        return ans
    
    
# This solution works - optimization - no need to check if best length is larger than the current one or 
# best length == current length but the answer word is smaller than the current word:

class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        longest = 0
        ans = ""
        for word in d:
            if len(word) < longest:
                continue
            elif len(word) == longest and ans < word:
                continue
            idx1 = idx2 = 0
            while idx1 < len(word) and idx2 < len(s):
                if word[idx1] == s[idx2]:
                    idx1 +=1
                    idx2 +=1
                else:
                    idx2+=1
            if idx1 >= len(word):
                if longest < len(word):
                    longest = len(word)
                    ans = word
                elif longest == len(word):
                    longest = len(word)
                    if not ans or ans > word:
                        ans = word
        return ans