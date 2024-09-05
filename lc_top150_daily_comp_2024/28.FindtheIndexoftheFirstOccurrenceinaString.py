'''
28. Find the Index of the First Occurrence in a String
Solved
Easy
Topics
Companies
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        for start in range(len(haystack)):
            if haystack[start] == needle[0] and len(needle) <= len(haystack)-1 - start + 1:
                i = start + 1
                for j in range(1, len(needle)):
                    if needle[j] != haystack[i]:
                        break
                    i += 1
                else:
                    return start
        return -1         
    
# Time: O(N*M)
# Space: O(1)

# Clean approach - slicing. The slicing does not break even if index is out of range as we are creating a new list

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack)):
            # haystack[i:i+len(needle)] <- slicing does not break even if index is out of range
            if haystack[i:i+len(needle)] == needle:
                    return i
        return -1         
    
# Time: O(N*M)
# Space: O(N*M) <- slicing creates a new list for the size of M which is N times

# N is the haystack list length
# M is the needle list length