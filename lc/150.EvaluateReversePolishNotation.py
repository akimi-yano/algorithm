# 150. Evaluate Reverse Polish Notation

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, /. Each operand may be an integer or another expression.

# Note:

# Division between two integers should truncate toward zero.
# The given RPN expression is always valid. That means the expression would always evaluate to a 
# result and there won't be any divide by zero operation.
# Example 1:

# Input: ["2", "1", "+", "3", "*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: ["4", "13", "5", "/", "+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# Output: 22
# Explanation: 
#   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# ________________________________________________________________________________________________________

# ---difference between isdigit() and isnumeric()---

# Strings have a great method called “isdigit” that we can run, to tell us whether a string contains 
# only digits (0-9), or if it contains something else. For example:

# >>> '1234'.isdigit()
# True

# >>> '1234 '.isdigit()  # space at the end
# False

# >>> '1234a'.isdigit()  # letter at the end
# False

# >>> 'a1234'.isdigit()  # letter at the start
# False

# >>> '12.34'.isdigit()  # decimal point
# False

# >>> ''.isdigit()   # empty string
# False



# It’s actually pretty straightforward, but took some time for me to find out: Bascially, str.isdigit 
# only returns True for what I said before, strings containing solely the digits 0-9.

# By contrast, str.isnumeric returns True if it contains any numeric characters. When I first read 
# this, I figured that it would mean decimal points and minus signs — but no! It’s just the digits 0-9, 
# plus any character from another language that’s used in place of digits.

# For example, we’re used to writing numbers with Arabic numerals. But there are other languages that 
# traditionally use other characters. For example, in Chinese, we count 1, 2, 3, 4, 5 as 一，二，三，四， 
# 五. It turns out that the Chinese characters for numbers will return False for str.isdigit, but True 
# for str.isnumeric, behaving differently from their 0-9 counterparts:

# >>> '12345'.isdigit()
# True

# >>> '12345'.isnumeric()
# True

# >>> '一二三四五'.isdigit()
# False

# >>> '一二三四五'.isnumeric()
# True

# _______________________________________________________________________________________________________
# my first solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem.isdigit() or (elem[0] in '+-' and elem[1:].isdigit()):
                stack.append(elem)
            else:
                b = stack.pop()
                a = stack.pop()
                if elem == "+":
                    val = int(a)+int(b)
                elif elem == "-":
                    val = int(a)-int(b)
                elif elem == "*":
                    val = int(a)*int(b)
                elif elem == "/":
                    val = int(int(a)/int(b)) # important !!!
                stack.append(val)
                # print(elem, a, b, val)
        ans = stack.pop()
        return ans
    
    # idea :
    #     use stack !
    #     if its number push it to the stack
    #     if its an operator do the operation by 2 numbers (get them by popping twice) and push the value back
    #     the last value left in the stack is the answer
    
    
# Note:
# -Division between two integers should truncate toward zero.  --> return integer after division by rounding down (not just smaller value) -> use int()
# -The given RPN expression is always valid. That means the expression would 
# always evaluate to a result and there won't be any divide by zero operation. -> always valid yes !

# hint video if you get stuck! : https://www.youtube.com/watch?v=qN8LPIcY6K4


# other Solution
def evalRPN(self, tokens):
    stack = []
    for t in tokens:
        if t not in ["+", "-", "*", "/"]:
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == "+":
                stack.append(l+r)
            elif t == "-":
                stack.append(l-r)
            elif t == "*":
                stack.append(l*r)
            else:
                # here take care of the case like "1/-22",
                # in Python 2.x, it returns -1, while in 
                # Leetcode it should return 0
                if l*r < 0 and l % r != 0:
                    stack.append(l/r+1)
                else:
                    stack.append(l/r)
    return stack.pop()




# optimized my code
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem.isdigit() or (elem[0] in '+-' and elem[1:].isdigit()):
                stack.append(elem)
            else:
                b = stack.pop()
                a = stack.pop()
                if elem == "+":
                    stack.append(int(a)+int(b))
                elif elem == "-":
                    stack.append(int(a)-int(b))
                elif elem == "*":
                    stack.append(int(a)*int(b))
                elif elem == "/":
                    stack.append(int(int(a)/int(b)))
          
        ans = stack.pop()
        return ans