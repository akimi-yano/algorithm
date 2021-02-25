# 856. Score of Parentheses
# Medium

# 1867

# 64

# Add to List

# Share
# Given a balanced parentheses string S, compute the score of the string based on the following rule:

# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: "()"
# Output: 1
# Example 2:

# Input: "(())"
# Output: 2
# Example 3:

# Input: "()()"
# Output: 2
# Example 4:

# Input: "(()(()))"
# Output: 6
 

# Note:

# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50


# This solution works:

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        for elem in S:
            if elem == "(":
                stack.append(elem)
            elif elem == ")":
                total = 0
                while stack and stack[-1] != "(":
                    total += stack.pop()
                if stack and stack[-1] == "(":
                    stack.pop()
                    if total > 0:
                        stack.append(2 * total)
                    else:
                        stack.append(1)
        return sum(stack)



# This solution works:

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        ans = 0
        multiplier = 1
        prev = ''
        for elem in S:
            if elem == "(":
                multiplier *= 2
            else:
                multiplier //= 2
                if prev == "(":
                    ans += multiplier
            prev = elem
        return ans
