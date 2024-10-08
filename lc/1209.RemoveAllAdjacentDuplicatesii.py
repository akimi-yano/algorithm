# 1209. Remove All Adjacent Duplicates in String II
# Medium

# 1437

# 33

# Add to List

# Share
# You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

# We repeatedly make k duplicate removals on s until we no longer can.

# Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

# Example 1:

# Input: s = "abcd", k = 2
# Output: "abcd"
# Explanation: There's nothing to delete.
# Example 2:

# Input: s = "deeedbbcccbdaa", k = 3
# Output: "aa"
# Explanation: 
# First delete "eee" and "ccc", get "ddbbbdaa"
# Then delete "bbb", get "dddaa"
# Finally delete "ddd", get "aa"
# Example 3:

# Input: s = "pbbcggttciiippooaais", k = 2
# Output: "ps"
 

# Constraints:

# 1 <= s.length <= 105
# 2 <= k <= 104
# s only contains lower case English letters.


# This approach does not work - TLE:

# class Solution:
#     def removeDuplicates(self, s: str, k: int) -> str:
#         stack = []
#         for c in s:
#             stack.append(c)
#             elem = stack[-k:]
#             if len(elem) < k:
#                 continue
#             if len(set(elem)) == 1:
#                 temp = k
#                 while temp:
#                     stack.pop()
#                     temp -= 1
#         return "".join(stack)
                    

# This solution works:

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[None, 1]]
        for c in s:
            if stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            stack[-1][1] =  stack[-1][1] % k
            if stack[-1][1] == 0:
                stack.pop()
        
        return "".join([char * freq for char, freq in stack[1:]])
                    