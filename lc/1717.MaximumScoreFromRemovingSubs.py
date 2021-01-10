# 1717. Maximum Score From Removing Substrings
# Medium

# 78

# 10

# Add to List

# Share
# You are given a string s and two integers x and y. You can perform two types of operations any number of times.

# Remove substring "ab" and gain x points.
# For example, when removing "ab" from "cabxbae" it becomes "cxbae".
# Remove substring "ba" and gain y points.
# For example, when removing "ba" from "cabxbae" it becomes "cabxe".
# Return the maximum points you can gain after applying the above operations on s.



# Example 1:

# Input: s = "cdbcbbaaabab", x = 4, y = 5
# Output: 19
# Explanation:
# - Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
# - Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
# - Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
# - Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
# Total score = 5 + 4 + 5 + 5 = 19.
# Example 2:

# Input: s = "aabbaaxybbaabb", x = 5, y = 4
# Output: 20


# Constraints:

# 1 <= s.length <= 105
# 1 <= x, y <= 104
# s consists of lowercase English letters.

# This solution works! count up!

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        stack = []
        cur = []
        for c in s:
            if c in ('a', 'b'):
                cur.append(c)
            else:
                if len(cur) > 1:
                    stack.append("".join(cur))
                cur = []    
        if len(cur) > 1:
            stack.append("".join(cur))
        
        total = 0
        for subs in stack:
            b_count = a_count = 0
            for char in subs:
                if char == 'a':
                    if y > x and b_count:
                        b_count -= 1
                        total += y
                    else:
                        a_count += 1
                elif char == 'b':
                    if not(y > x) and a_count:
                        a_count -= 1
                        total += x
                    else:
                        b_count += 1
            if y > x:
                total += x * min(a_count, b_count)
            else:
                total += y * min(a_count, b_count)
        return total
                    
            

# This approach does not work
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         def helper(i):
#             if i > len(s)-2:
#                 return 0
#             points = 0
#             sequence = s[i:i+2]
#             if sequence == "ab":
#                 points = max(points, x + helper(i+1)) 
#             elif sequence == "ba":
#                 points = max(points, y + helper(i+1)) 
#             points = max(points, helper(i+1)) 
#             return points
#         return helper(0)

# This approach does not work
# class Solution:
#     def maximumGain(self, s: str, x: int, y: int) -> int:
#         first = second = None
#         if x > y:
#             first, second = "ab", "ba"
#         else:
#             first, second = "ba", "ab"
        
#         memo = {first:[], second:[]}
#         for i in range(len(s)-1):
#             if s[i:i+2] == first:
#                 memo[first].append((i,i+1))
#             elif s[i:i+2] == second:
#                 memo[second].append((i,i+1))
        
#         total = 0

#         for start, end in memo[first]:
#             total += max(x, y)
#             nextstart = start-1
#             nextend = end+1
#             while nextstart >= 0 and nextend < len(s) and s[nextstart] + s[nextend] in ("ab", "ba"):
#                 if s[nextstart] + s[nextend] == first:
#                     total += max(x, y)
#                 elif s[nextstart] + s[nextend] == second:
#                     total += min(x, y)
#                 nextstart -= 1
#                 nextend += 1

#         for start, end in memo[second]:
#             total += min(x, y)
#             nextstart = start-1
#             nextend = end+1
#             while nextstart >= 0 and nextend < len(s) and s[nextstart] + s[nextend] in ("ab", "ba"):
#                 if s[nextstart] + s[nextend] == first:
#                     total += max(x, y)
#                 elif s[nextstart] + s[nextend] == second:
#                     total += min(x, y)
#                 nextstart -= 1
#                 nextend += 1

#         return total
