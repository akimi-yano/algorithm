'''
916. Word Subsets
Attempted
Medium
Topics
Companies
You are given two string arrays words1 and words2.

A string b is a subset of string a if every letter in b occurs in a including multiplicity.

For example, "wrr" is a subset of "warrior" but is not a subset of "world".
A string a from words1 is universal if for every string b in words2, b is a subset of a.

Return an array of all the universal strings in words1. You may return the answer in any order.

 

Example 1:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
Output: ["facebook","google","leetcode"]
Example 2:

Input: words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
Output: ["apple","google","leetcode"]
 

Constraints:

1 <= words1.length, words2.length <= 104
1 <= words1[i].length, words2[i].length <= 10
words1[i] and words2[i] consist only of lowercase English letters.
All the strings of words1 are unique.
'''

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        goal = Counter()
        for word in words2:
            cur = Counter()
            for char in word:
                cur[char] += 1
            for char, count in cur.items():
                goal[char] = max(goal[char], cur[char])
        
        ans = []
        for word in words1:
            cur = Counter(word)
            for char, count in goal.items():
                if cur[char] < count:
                    is_valid = False
                    break
            else:
                ans.append(word)
        return ans