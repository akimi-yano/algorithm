# 20. Valid Parentheses
# Easy

# 6590

# 269

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
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

# This solution works !
# Time: O(N)
# Space: O(N)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(":")", "{":"}", "[":"]"}
        for elem in s:
            if elem in pairs:
                stack.append(elem)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if pairs[opening] != elem:
                    return False
        return not stack