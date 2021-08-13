# 49. Group Anagrams
# Medium

# 6460

# 250

# Add to List

# Share
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]
 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lower-case English letters.

# This solution works:

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_words = {}
        for word in strs:
            word_list = list(word)
            word_list.sort()
            key = "".join(word_list)
            if key not in all_words:
                all_words[key] = []
            all_words[key].append(word)
        
        ans = list(all_words.values())
        return ans