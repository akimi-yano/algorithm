# 227. Basic Calculator II
# Medium

# 3287

# 472

# Add to List

# Share
# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5
 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0, 231 - 1].
# The answer is guaranteed to fit in a 32-bit integer.


# This solution works:


class Solution:
    def calculate(self, s: str) -> int:
        # 1st pass: handle numbers
        stack = []
        num = 0
        for elem in s:
            if elem == " ":
                pass
            elif elem in ("*", "/"):
                stack.append(num)
                num = 0
                stack.append(elem)
            elif elem in ("+", "-"):
                stack.append(num)
                num = 0
                stack.append(elem)
            else:
                num *= 10
                num += int(elem)
        stack.append(num)
        
        # 2nd pass: handle * and /
        new_stack = []
        i = 0
        while i < len(stack):
            if stack[i] == "*":
                new_stack.append(new_stack.pop() * stack[i+1])
                i += 1
            elif stack[i] == "/":
                new_stack.append(new_stack.pop() // stack[i+1])
                i +=1
            else:
                new_stack.append(stack[i])
            i +=1
        
        # 3rd pass: handle + and -
        last_stack = []
        i = 0
        while i < len(new_stack):
            if new_stack[i] == "+":
                last_stack.append(last_stack.pop() + new_stack[i+1])
                i += 1
            elif new_stack[i] == "-":
                last_stack.append(last_stack.pop() - new_stack[i+1])
                i +=1
            else:
                last_stack.append(new_stack[i])
            i +=1
            
        return last_stack[0]