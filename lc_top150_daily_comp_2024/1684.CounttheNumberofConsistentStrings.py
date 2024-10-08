'''
1684. Count the Number of Consistent Strings
Solved
Easy
Topics
Companies
Hint
You are given a string allowed consisting of distinct characters and an array of strings words. A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

 

Example 1:

Input: allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent since they only contain characters 'a' and 'b'.
Example 2:

Input: allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
Output: 7
Explanation: All strings are consistent.
Example 3:

Input: allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent.
 

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
'''

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        goal = set(allowed)
        ans = 0
        for word in words:
            for char in set(word):
                if char not in goal:
                    break
            else:
                ans += 1
        return ans
    
# Time: O(N*W) where N is length of words * W is length of words[i]
# Space: O(A) or O(W) A (allowed)is 26 at max and W (words[i]) is 10 at max. Whichever is larger.

# This solution works and its an optimization fofr space complexity:

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        goal = 0
        for char in allowed:
            goal = (1 << (ord(char) - ord('a'))) | goal

        ans = 0
        for word in words:
            for char in word:
                if not ((1 << (ord(char) - ord('a'))) & goal):
                    break
            else:
                ans += 1
        return ans

# Time: O(N*W)
# Space: O(1)

# We could also do like this to check the bit ->:  bit = (allowed_bits >> (ord(char) - ord("a"))) & 1 