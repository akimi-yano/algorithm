# 438. Find All Anagrams in a String
# Medium

# 6188

# 235

# Add to List

# Share
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

# Example 1:

# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input: s = "abab", p = "ab"
# Output: [0,1,2]
# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".
 

# Constraints:

# 1 <= s.length, p.length <= 3 * 104
# s and p consist of lowercase English letters.


# This soluion works:


from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        goal= Counter(p)
        cur = Counter()
        ans = []
        count = 0
        for i in range(len(s)):
            cur[s[i]] += 1
            count += 1
            if count == len(p):
                if goal == cur:
                    ans.append(i+1-count)
                cur[s[i+1-count]] -= 1
                count -=1
        return ans
        '''
         
        s "cbaebabacd"
        p "abc"
        
        goal {a:1, b:1, c:0}
        cur {c:1, b:1, a:1}
        ans []
        count 0 1 2 
        
        '''