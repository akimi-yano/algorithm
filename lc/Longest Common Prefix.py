# 14. Longest Common Prefix
# Easy

# 2911

# 1942

# Add to List

# Share
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

# Accepted
# 812,401
# Submissions
# 2,284,828



# THIS APPROACH WORKS:

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) < 1:
            return prefix

        first_word = strs[0]
        for i in range(len(first_word)):
            ith_character = first_word[i]
            for word in strs:
                if i >= len(word):
                    return prefix
                if word[i] != ith_character:
                    return prefix
            prefix += ith_character
        return prefix
        
        
        """
        pref_cand = None
        pref_longest = ""
       
    
    
        if strs == []:
            return pref_longest
        
        else:
            shortest_word = strs[0] 
            shortest_length = len(shortest_word)

            for word in strs:
                        if shortest_length > len(word):
                            shortest_length = len(word)

            for i in range(shortest_length):
                for word in strs:
                    if pref_cand == None:
                        pref_cand = word[i]
                    else:
                        if word[i] == pref_cand:
                            continue
                        else:
                            return pref_longest
                pref_longest += pref_cand
                pref_cand = None
            return pref_longest
            """
        
    
# Another Solution
 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 