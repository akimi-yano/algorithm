# 20. Valid Parentheses
# Easy

# 11739

# 516

# Add to List

# Share
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# This solution works:


class Solution:
    def isValid(self, s: str) -> bool:
        memo = {'(':')', '{':'}', '[':']'}
        stack = []
        for c in s:
            if c in memo:
                stack.append(c)
            else:
                if stack and stack[-1] in memo and memo[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        return not stack