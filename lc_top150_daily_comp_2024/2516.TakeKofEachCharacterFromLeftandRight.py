'''
2516. Take K of Each Character From Left and Right
Medium
Topics
Companies
Hint
You are given a string s consisting of the characters 'a', 'b', and 'c' and a non-negative integer k. Each minute, you may take either the leftmost character of s, or the rightmost character of s.

Return the minimum number of minutes needed for you to take at least k of each character, or return -1 if it is not possible to take k of each character.

 

Example 1:

Input: s = "aabaaaacaabc", k = 2
Output: 8
Explanation: 
Take three characters from the left of s. You now have two 'a' characters, and one 'b' character.
Take five characters from the right of s. You now have four 'a' characters, two 'b' characters, and two 'c' characters.
A total of 3 + 5 = 8 minutes is needed.
It can be proven that 8 is the minimum number of minutes needed.
Example 2:

Input: s = "a", k = 1
Output: -1
Explanation: It is not possible to take one 'b' or 'c' so return -1.
 

Constraints:

1 <= s.length <= 105
s consists of only the letters 'a', 'b', and 'c'.
0 <= k <= s.length
'''

from collections import Counter
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        def check_valid(cur):
            is_valid = True
            for char in ('a', 'b', 'c'):
                if cur[char] < k:
                    is_valid = False
                    break
            return is_valid

        original = Counter(s)
        rm = Counter()
        N = len(s)
        ans = N

        # keep track of the range for not using with left and right
        left = 0
        for right in range(N):
            rm[s[right]] += 1
            cur = original-rm
            valid = check_valid(cur)
            
            while not valid and left <= right:
                rm[s[left]] -= 1
                cur = original-rm
                valid = check_valid(cur)
                left += 1

            if valid:
                ans = min(ans, N-(right-left+1))
        return ans if valid else -1

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:

        limits = {c: s.count(c) - k for c in 'abc'}
        if any(x < 0 for x in limits.values()):
            return -1
        
        cur = {c: 0 for c in 'abc'}
        ans = l = 0
        for r, c in enumerate(s):
            cur[c] += 1
            # if the cur[c] <= limits[c], it means that we are using the ones that we cannot use for removing.
            while cur[c] > limits[c]:
                cur[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        
        return len(s) - ans