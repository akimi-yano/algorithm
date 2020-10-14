# 1021. Remove Outermost Parentheses
# Easy

# 599

# 699

# Add to List

# Share
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

# A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

# Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

# Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.



# Example 1:

# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
# After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
# Example 2:

# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".
# Example 3:

# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".


# Note:

# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string


# This solution works !!!

'''
can append if the count is not 0
'''

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        count = 0
        ans = []
        for elem in S:
            if elem =="(":
                if count > 0:
                    ans.append("(")
                count += 1
            elif elem == ")":
                count -= 1
                if count > 0:
                    ans.append(")")
        return "".join(ans)
            

