# 1625. Lexicographically Smallest String After Applying Operations
# Medium

# 27

# 77

# Add to List

# Share
# You are given a string s of even length consisting of digits from 0 to 9, and two integers a and b.

# You can apply either of the following two operations any number of times and in any order on s:

# Add a to all odd indices of s (0-indexed). Digits post 9 are cycled back to 0. For example, if s = "3456" and a = 5, s becomes "3951".
# Rotate s to the right by b positions. For example, if s = "3456" and b = 1, s becomes "6345".
# Return the lexicographically smallest string you can obtain by applying the above operations any number of times on s.

# A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b. For example, "0158" is lexicographically smaller than "0190" because the first position they differ is at the third letter, and '5' comes before '9'.

 

# Example 1:

# Input: s = "5525", a = 9, b = 2
# Output: "2050"
# Explanation: We can apply the following operations:
# Start:  "5525"
# Rotate: "2555"
# Add:    "2454"
# Add:    "2353"
# Rotate: "5323"
# Add:    "5222"
# ​​​​​​​Add:    "5121"
# ​​​​​​​Rotate: "2151"
# ​​​​​​​Add:    "2050"​​​​​​​​​​​​
# There is no way to obtain a string that is lexicographically smaller then "2050".
# Example 2:

# Input: s = "74", a = 5, b = 1
# Output: "24"
# Explanation: We can apply the following operations:
# Start:  "74"
# Rotate: "47"
# ​​​​​​​Add:    "42"
# ​​​​​​​Rotate: "24"​​​​​​​​​​​​
# There is no way to obtain a string that is lexicographically smaller then "24".
# Example 3:

# Input: s = "0011", a = 4, b = 2
# Output: "0011"
# Explanation: There are no sequence of operations that will give us a lexicographically smaller string than "0011".
# Example 4:

# Input: s = "43987654", a = 7, b = 3
# Output: "00553311"
 

# Constraints:

# 2 <= s.length <= 100
# s.length is even.
# s consists of digits from 0 to 9 only.
# 1 <= a <= 9
# 1 <= b <= s.length - 1







# This approach does not work:

# class Solution:
#     def findLexSmallestString(self, s: str, a: int, b: int) -> str:
#         '''
#         rotate first to get the min number on the left
#         then keep adding until the number after addition is larger than 9 - while
#         '''

#         self.s_list = [int(elem) for elem in s]
#         while True:
#             # rotation
#             if self.s_list[b] < self.s_list[0]:
#                 self.rotate(b, len(s)-1)
#                 self.rotate(0, b-1)
#                 self.rotate(0, len(s)-1)
                
#             # addition
#             elif (self.s_list[1] + a ) > 9:
#                 for i in range(1, len(self.s_list), 2):
#                     self.s_list[i] = (self.s_list[i] + a) % 10
#             else:
#                 break

#         return "".join([str(elem) for elem in self.s_list])

#     def rotate(self, start, end):
#         while start < end:
#             self.s_list[start], self.s_list[end] = self.s_list[end], self.s_list[start]
#             start += 1
#             end -= 1
            
            
# This solution works !

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        self.seen = set([])
        self.a = a
        self.b = b

        self.helper(s)

        return min(self.seen)
    
    def helper(self, s):
        if s in self.seen:
            return
        self.seen.add(s)

        # option 1: add a to the odd indexes
        chars = [int(c) for c in s]
        for i in range(1, len(chars), 2):
            chars[i] += self.a
            chars[i] %= 10
        s2 = ''.join([str(c) for c in chars])
        self.helper(s2)
        
        # option 2: rotate
        s3 = s[-self.b:] + s[:-self.b]
        self.helper(s3)