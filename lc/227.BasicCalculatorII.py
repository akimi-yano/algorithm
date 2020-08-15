# 227. Basic Calculator II

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


# this solution works !

def calculate(self, s):
    if not s:
        return "0"
    stack, num, sign = [], 0, "+"
    for i in xrange(len(s)):
        if s[i].isdigit():
            num = num*10+ord(s[i])-ord("0")
        if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
            if sign == "-":
                stack.append(-num)
            elif sign == "+":
                stack.append(num)
            elif sign == "*":
                stack.append(stack.pop()*num)
            else:
                tmp = stack.pop()
                if tmp//num < 0 and tmp%num != 0:
                    stack.append(tmp//num+1)
                else:
                    stack.append(tmp//num)
            sign = s[i]
            num = 0
    return sum(stack)


# this solution is more intuitive with step by step (3 steps)!

class Solution:
    def calculate(self, s: str) -> int:
        symbols = ['+', '-', '*', '/']
        # 1st pass: make a formatted array like this ["3", "/", "2"]
        elements = []
        cur = ''
        for c in s:
            if c in symbols:
                # If there is a previous number, append it first
                if cur != '':
                    elements.append(int(cur))
                    cur = ''
                elements.append(c)
            elif c == ' ':
                continue
            else:
                cur += c
        elements.append(int(cur))
        # print(elements)
        
        # 2nd pass: add everything to stack until I see x or /
        # if I see them process it and add back to stack
        after_mul_div = deque([])
        symbol = None
        for element in elements:
            if element in symbols:
                symbol = element
            else:
                if symbol is None:
                    after_mul_div.append(element)
                else:
                    if symbol == '*':
                        result = after_mul_div.pop() * element
                        after_mul_div.append(result)
                    elif symbol == '/':
                        result = after_mul_div.pop() // element
                        after_mul_div.append(result)
                    else:
                        after_mul_div.append(symbol)
                        after_mul_div.append(element)
                    symbol = None
        # print(after_mul_div)
        
        # 3rd pass: pop 3 and process it until there is only 1 element left
        while len(after_mul_div) > 1:
            num1, symbol, num2 = after_mul_div.popleft(), after_mul_div.popleft(), after_mul_div.popleft()
            if symbol == '+':
                after_mul_div.appendleft(num1 + num2)
            else:
                after_mul_div.appendleft(num1 - num2)
        return after_mul_div[0]
        
