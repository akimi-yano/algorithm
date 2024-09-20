'''
214. Shortest Palindrome
Solved
Hard
Topics
Companies
You are given a string s. You can convert s to a 
palindrome
 by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 104
s consists of lowercase English letters only.
'''

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        "aacecaaa" (8)
        i : 0~9
        8-i
          8 7 6 5 4 3 2 1 0 -1       
    
        aaacecaa
        '''
        reversed_s = s[::-1]
        for i in range(len(s)+1):
            if s[:len(s)-i] == reversed_s[i:]:
                return reversed_s[:i] + s


# Time: O(N^2)
# Space: O(N)

'''
A palindrome reads the same forwards and backwards. 
Therefore, the challenge is to identify the longest prefix of the original string that can be 
extended to a full palindrome by only adding characters at the start.
If a prefix matches a suffix of the reversed string, it’s part of a palindrome.
Once we find the longest palindromic prefix, we need to reverse the rest of the string 
(the part not included in the prefix) and add this reversed part to the start of the original string. 
This gives us the shortest possible palindrome.
'''