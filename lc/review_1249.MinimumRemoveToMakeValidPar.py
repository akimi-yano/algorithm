# 1249. Minimum Remove to Make Valid Parentheses
# Medium

# 3755

# 70

# Add to List

# Share
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
 

# Constraints:

# 1 <= s.length <= 105
# s[i] is either'(' , ')', or lowercase English letter.


# This solution works:


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        invalid = []
        for i, elem in enumerate(s):
            if elem == "(":
                stack.append(i)
            elif elem == ")":
                if stack and s[stack[-1]] == "(":
                    stack.pop()
                else:
                    invalid.append(i)
        
        # the stack needs to be empty so whatever is left is invalid
        while stack:
            invalid.append(stack.pop())
        
        invalid_set = set(invalid)
        
        ans = []
        for i, elem in enumerate(s):
            if i not in invalid_set:
                ans.append(elem)
        return "".join(ans)
                
        