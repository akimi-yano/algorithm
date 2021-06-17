# 22. Generate Parentheses
# Medium

# 8309

# 342

# Add to List

# Share
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8

# This solution works:
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def is_valid(temp):
            stack = []
            for elem in temp:
                if elem == "(":
                    stack.append(elem)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False
            return not stack
        
        def helper(cur):
            nonlocal ans
            if len(cur) == n*2:
                if is_valid(cur):
                    ans.append("".join(cur))
                return
            cur.append("(")
            helper(cur)
            cur.pop()
            cur.append(")")
            helper(cur)
            cur.pop()
        ans = []
        helper([])
        return ans
                