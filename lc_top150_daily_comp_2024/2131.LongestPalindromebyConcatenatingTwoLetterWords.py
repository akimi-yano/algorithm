'''
2131. Longest Palindrome by Concatenating Two Letter Words
Medium
Topics
Companies
Hint
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

 

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
Example 2:

Input: words = ["ab","ty","yt","lc","cl","ab"]
Output: 8
Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
Note that "lcyttycl" is another longest palindrome that can be created.
Example 3:

Input: words = ["cc","ll","xx"]
Output: 2
Explanation: One longest palindrome is "cc", of length 2.
Note that "ll" is another longest palindrome that can be created, and so is "xx".
 

Constraints:

1 <= words.length <= 105
words[i].length == 2
words[i] consists of lowercase English letters.
'''

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        '''
        For words that are not palindromes (e.g., "ab"), look for their reverse ("ba") and form pairs.
        For palindromic words (e.g., "aa"), use as many pairs as possible (even count), and keep track if an odd one can go in the center.

        Each pair contributes 4 characters to the result.
        If there's one palindromic word left (like one "aa"), it can be placed in the middle, adding 2 to the total length.
        '''
        freq = Counter(words)
        ans = 0
        has_center = False

        for word in list(freq.keys()):
            rev = word[::-1]
            if word == rev:
                pairs = freq[word] // 2
                ans += pairs * 4
                freq[word] -= pairs * 2
                if freq[word] == 1:
                    has_center = True
            else:
                if rev in freq:
                    pairs = min(freq[word], freq[rev])
                    ans += pairs * 4
                    freq[word] -= pairs
                    freq[rev] -= pairs

        if has_center:
            ans += 2

        return ans