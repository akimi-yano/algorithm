# 32. Longest Valid Parentheses
# Hard

# 7938

# 265

# Add to List

# Share
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.


# This solution works:


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        arr = []
        for i, c in enumerate(s):
            if c == "(":
                if not arr:
                    arr.append(i-1)
                arr.append(i)
            else:
                if not arr:
                    continue
                arr.pop()
                if not arr:
                    continue
                best = max(best, i - arr[-1])
        return best
