'''
3291. Minimum Number of Valid Strings to Form Target I
Medium

9

3

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
1 <= words[i].length <= 5 * 103
The input is generated such that sum(words[i].length) <= 105.
words[i] consists only of lowercase English letters.
1 <= target.length <= 5 * 103
target consists only of lowercase English letters.
'''

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        # Build trie
        root = {}
        for word in words:
            if word[0] not in root:
                root[word[0]] = {}
            cur = root[word[0]]
            for c in word[1:]:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
        # print(root)
   
        N = len(target)
        # Keep track of start index which is the index that we start fresh using the root of trie
        @cache
        def helper(start):
            if start > N-1:
                return 0

            min_steps = float('inf')
            cur = root
            # this j also checks from the start index and check how far you could go without restarting with the trie root and incrementing the count by 1
            for j in range(start, N):
                if target[j] not in cur:
                    break
                cur = cur[target[j]]
                # The recursion call is for the case to start with the trie root again so it adds one step
                min_steps = min(min_steps, 1 + helper(j+1))
            return min_steps

        ans = helper(0)
        return ans if ans != float('inf') else -1