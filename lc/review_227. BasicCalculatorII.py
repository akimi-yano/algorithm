# 227. Basic Calculator II
# Medium

# 1889

# 312

# Add to List

# Share
# Implement a basic calculator to evaluate a simple expression string.

# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

# Example 1:

# Input: "3+2*2"
# Output: 7
# Example 2:

# Input: " 3/2 "
# Output: 1
# Example 3:

# Input: " 3+5 / 2 "
# Output: 5
# Note:

# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.


# This approach does not work 

# class Solution:
#     def calculate(self, s: str) -> int:
#         stack = []
#         sign = None
#         for c in s:
#             if c == "*":
#                 sign = "*"
#             elif c == "/":
#                 sign = "/"
#             else:
#                 if c == " ":
#                     continue
#                 elif not sign:
#                     stack.append(c)
#                 else:
#                     num1 = int(stack.pop()) 
#                     num2 = int(c)
#                     if sign == "*":
#                         stack.append(num1 * num2)
#                     else:
#                         if num2 != 0:
#                             stack.append(num1 // num2)
#                     sign = None
        
#         sign = None
#         stack2 = []
#         for elem in stack:
#             if elem == "+":
#                 sign = "+"
#             elif elem == "-":
#                 sign = "-"
#             else:
#                 if not sign:
#                     stack2.append(int(elem)) 
#                 else:
#                     num1 = int(stack2.pop())
#                     num2 = int(elem)
#                     if sign == "+":
#                         stack2.append(num1 + num2)
#                     else:   
#                         stack2.append(num1 - num2)
#                     sign = None
            
#         return stack2[0]
        
# This solution works !:
'''
put everything in stack
If c is * or /,  the  previous symbol has to be * or / to also do the math operation
If c is + pr -, do the previous operation first
and keep moving forward until there is only 1 thing left
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        for c in s:
            if c.isdigit():
                if stack and type(stack[-1]) == int:
                    stack.append(stack.pop() * 10 + int(c))
                else:
                    stack.append(int(c))
            else:         
                if c in ["+", '-']:
                    while len(stack) >= 3:
                        stack.append(self.helper(stack.pop(), stack.pop(), stack.pop()))
                    stack.append(c)
                elif c in ["*", "/"]:
                    while len(stack) >= 3 and stack[-2] in ["*", "/"]:
                        stack.append(self.helper(stack.pop(), stack.pop(), stack.pop()))
                    stack.append(c)
        while len(stack) > 1:
            stack.append(self.helper(stack.pop(), stack.pop(), stack.pop()))
        return stack[0]
    
    def helper(self, number2, symbol, number1):
        if symbol == '+':
            return number1 + number2
        if symbol == '-':
            return number1 - number2
        if symbol == '*':
            return number1 * number2
        if symbol == '/':
            return number1 // number2