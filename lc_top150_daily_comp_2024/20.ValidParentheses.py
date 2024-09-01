'''
20. Valid Parentheses
Solved
Easy
Topics
Companies
Hint
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

# This solution works:

class Solution:
    def isValid(self, s: str) -> bool:
        open_close_pairs = {'(':')', '{':'}', '[':']'}
        stack = []
        for elem in s:
            # elem is open paren
            if elem in open_close_pairs:
                stack.append(elem)
            # elem is close paren
            else:
                if not stack or elem != open_close_pairs[stack.pop()]:
                    return False
        return not stack
    
# Time: O(N)
# Space: O(N) 