# 438. Find All Anagrams in a String
# Medium

# 3467

# 182

# Add to List

# Share
# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
# Example 2:

# Input:
# s: "abab" p: "ab"

# Output:
# [0, 1, 2]

# Explanation:
# The substring with start index = 0 is "ab", which is an anagram of "ab".
# The substring with start index = 1 is "ba", which is an anagram of "ab".
# The substring with start index = 2 is "ab", which is an anagram of "ab".



# This approach does not work: 

# from collections import Counter 
# class Solution:
#     def findAnagrams(self, s: str, p: str) -> List[int]:
#         p_count = Counter(p)
#         s_count = Counter()
#         start = 0
#         ans = []
#         for i in range(len(s)):
#             if s_count == p_count:
#                 ans.append(start)
#                 s_count = Counter()
#                 start = i
                
#             if s[i] in p_count:
#                 if s_count[s[i]] < p_count[s[i]]:
#                     s_count[s[i]] +=1
#                 else:
#                     s_count = Counter()
#                     s_count[s[i]] +=1
#                     start = i

#             else:
#                 s_count = Counter()
#                 start = i+1



#         return ans
                

# This approach works :
'''
Maintain a window of len(p) in s, and slide to right until finish. Time complexity is O(len(s)).
'''
'''
s: "cbaebabacd" p: "abc"


Output:
[0, 6]

sliding window 
start with window side 2 and add one more in the loop and remove one more
'''



from collections import Counter
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        pCounter = Counter(p)
        # start the dictionary with the size of length of p - 1
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
                
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
    