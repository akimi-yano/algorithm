# 567. Permutation in String
# Medium

# 4394

# 126

# Add to List

# Share
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:

# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false
 

# Constraints:

# 1 <= s1.length, s2.length <= 104
# s1 and s2 consist of lowercase English letters.


# This solution works:


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        goal = {}
        goal_count = len(s1)
        for char in s1:
            if char not in goal:
                goal[char] = 0
            goal[char] += 1
        
        cur = {}
        cur_count = 0
        for i in range(len(s2)):
            if s2[i] not in cur:
                cur[s2[i]] = 0
            cur[s2[i]] += 1
            cur_count += 1
            if goal_count < cur_count:
                newi = i+1-cur_count
                cur[s2[newi]] -= 1
                cur_count -= 1
                if cur[s2[newi]] <= 0:
                    del cur[s2[newi]]
            if goal_count == cur_count:
                if goal == cur:
                    return True
        return False