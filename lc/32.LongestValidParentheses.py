# 32. Longest Valid Parentheses
# Hard

# 4879

# 181

# Add to List

# Share
# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:

# Input: s = ""
# Output: 0
 

# Constraints:

# 0 <= s.length <= 3 * 104
# s[i] is '(', or ')'.

# This solution works - keep track of the index to know which one is the last index before failing:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        best = 0
        arr = []
        for i, c in enumerate(s):
            if c == "(":
                if not arr:
                    arr.append(i-1)
                arr.append(i)
            else:
                if not arr:
                    continue
                arr.pop()
                if not arr:
                    continue
                best = max(best, i - arr[-1])
        return best
    
# This approach does not work - just keeping track of the counts with variables wont work as you lose track
# of the index - we need stack at least:

# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         total = 0
#         opens = 0
#         best = 0
#         for elem in s:
#             if elem == "(":
#                 opens += 1
#             else:
#                 if opens:
#                     total += 2
#                     opens -= 1
#                 else:
#                     total = 0
#                 best = max(best, total)
#         return best
                