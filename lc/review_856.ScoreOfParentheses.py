# 856. Score of Parentheses
# Medium

# 3273

# 97

# Add to List

# Share
# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
 

# Example 1:

# Input: s = "()"
# Output: 1
# Example 2:

# Input: s = "(())"
# Output: 2
# Example 3:

# Input: s = "()()"
# Output: 2
 

# Constraints:

# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.


# This solution works:


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        "(((((())))))"
               12481632
        
        "(()(()))"
          1  12
           6
        '''
        stack = []
        ans = 0
        for elem in s:
            if elem == '(':
                if stack and stack[-1] != '(':
                    stack.append(stack.pop())
                stack.append(elem)
            else:
                if stack:
                    if stack[-1] == '(':
                        stack.pop() #remove "("
                        stack.append(1)
                    else:
                        cur = 0
                        while stack[-1] != '(':
                            cur += stack.pop()
                        stack.pop() #remove "("
                        stack.append(cur*2)

        while stack and stack[-1] != '(':
            ans += stack.pop()
        return ans