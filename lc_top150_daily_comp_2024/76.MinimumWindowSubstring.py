'''
76. Minimum Window Substring
Solved
Hard
Topics
Companies
Hint
Given two strings s and t of lengths m and n respectively, return the minimum window 
substring
 of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
 

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.
 

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

# This approach works!:

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        1 keep track of the minimum string (and just check the length) <- just keep track of the start and end index
        2 keep track of which character and how many are aleady found
        3 keep track of the goal of which character and how many
        
        ADOBECODEBANC
             r      e
        '''
        # 1) keep track of the min string indices
        best_start = 0
        best_end = len(s)-1

        # 2) keep track of the cur: char and count
        cur = Counter()

        # 3) keep track of the goal
        goal = Counter(t)
        rm = 0
        found = False
        for end in range(len(s)):
            cur[s[end]] += 1
            while cur & goal == goal:
                found = True
                if (best_end - best_start + 1) > (end - rm + 1):
                    best_end = end
                    best_start = rm
                cur[s[rm]] -= 1
                rm += 1
        return s[best_start:best_end+1] if found else ""
    
# TIME:O(S+T)
# SPACE:O(S+T)
