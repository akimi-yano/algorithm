'''
Valid Anagram


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for char in s:
            if char not in char_count:
                char_count[char] = 0
            char_count[char] += 1
        for char in t:
            if char not in char_count:
                return False
            char_count[char] -= 1
            if char_count[char] < 1:
                del char_count[char]
        return not char_count