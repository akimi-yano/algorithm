'''
3292. Minimum Number of Valid Strings to Form Target II
Hard

5

7

Add to List

Share
You are given an array of strings words and a string target.

A string x is called valid if x is a prefix of any string in words.

Return the minimum number of valid strings that can be concatenated to form target. If it is not possible to form target, return -1.

A prefix of a string is a substring that starts from the beginning of the string and extends to any point within it.

 

Example 1:

Input: words = ["abc","aaaaa","bcdef"], target = "aabcdabc"

Output: 3

Explanation:

The target string can be formed by concatenating:

Prefix of length 2 of words[1], i.e. "aa".
Prefix of length 3 of words[2], i.e. "bcd".
Prefix of length 3 of words[0], i.e. "abc".
Example 2:

Input: words = ["abababab","ab"], target = "ababaababa"

Output: 2

Explanation:

The target string can be formed by concatenating:

Prefix of length 5 of words[0], i.e. "ababa".
Prefix of length 5 of words[0], i.e. "ababa".
Example 3:

Input: words = ["abcdef"], target = "xyz"

Output: -1

 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 5 * 104
The input is generated such that sum(words[i].length) <= 105.
words[i] consists only of lowercase English letters.
1 <= target.length <= 5 * 104
target consists only of lowercase English letters.
'''

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        
        # The Knuth-Morris-Pratt (KMP) algorithm is a string-searching algorithm 
        # that finds all occurrences of a pattern string in a text string
        def KMP(pattern, text):
            k = 0
            LPS = [0] 
            # Computes the longest proper prefix which is also suffix (LPS) array for the KMP algorithm
            for i in range(1, len(pattern)):
                while k and pattern[k] != pattern[i]: 
                    k = LPS[k-1]
                if pattern[k] == pattern[i]: 
                    k += 1
                LPS.append(k)
            k = 0
            ans = []
            for i, ch in enumerate(text): 
                while k and (k == len(pattern) or pattern[k] != ch): k = LPS[k-1]
                if pattern[k] == ch: 
                    k += 1
                ans.append(k)
            # ans[i] is the length of the longest prefix of the pattern that matches a suffix ending at position i in the text.
            return ans

        N = len(target)
        vals = [set() for _ in range(N)]
        for word in words: 
            candidates = KMP(word, target)
            # print(candidates)
            for i, k in enumerate(candidates): 
                #  Add non-zero match lengths to the corresponding set in vals
                if k: 
                    vals[i].add(k)
            # print(vals)
        # Initialize a dynamic programming array dp with infinity values, setting the last element to 0.
        dp = [inf]*(N+1)
        dp[N] = 0 
        for i in range(N-1, -1, -1): 
            for k in vals[i]:
                # Fill the dp array from right to left. For each position i and each match length k at that position, update dp[i-k+1] with the minimum of its current value and 1 + dp[i+1]
                dp[i-k+1] = min(dp[i-k+1], 1 + dp[i+1])
        return dp[0] if dp[0] < inf else -1