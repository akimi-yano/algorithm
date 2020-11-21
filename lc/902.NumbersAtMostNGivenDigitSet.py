# 902. Numbers At Most N Given Digit Set
# Hard

# 381

# 58

# Add to List

# Share
# Given an array of digits, you can write numbers using each digits[i] as many times as we want.  For example, if digits = ['1','3','5'], we may write numbers such as '13', '551', and '1351315'.

# Return the number of positive integers that can be generated that are less than or equal to a given integer n.

 

# Example 1:

# Input: digits = ["1","3","5","7"], n = 100
# Output: 20
# Explanation: 
# The 20 numbers that can be written are:
# 1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
# Example 2:

# Input: digits = ["1","4","9"], n = 1000000000
# Output: 29523
# Explanation: 
# We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
# 81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
# 2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
# In total, this is 29523 integers that can be written using the digits array.
# Example 3:

# Input: digits = ["7"], n = 8
# Output: 1
 

# Constraints:

# 1 <= digits.length <= 9
# digits[i].length == 1
# digits[i] is a digit from '1' to '9'.
# All the values in digits are unique.
# 1 <= n <= 109

# This approach does not work 
# class Solution:
#     def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
#         def helper(i, num_str):

#             if num_str and int(num_str) > n:
#                 return
#             if i > len(digits)-1:
#                 return
#             if num_str:
#                 self.strings.add(num_str)
#             for k in range(len(digits)):
#                 helper(k, num_str+digits[i])
#             helper(i+1, num_str)
    
#         self.strings = set([])
#         helper(0, "")
#         print(self.strings)
#         return len(self.strings)


# This solution works !

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        self.digits = [int(d) for d in digits]
        self.D = len(self.digits)
        
        self.nlist = []
        while n:
            self.nlist.append(n % 10)
            n //= 10
        self.nlist.reverse()
        # print(self.nlist)
        self.N = len(self.nlist)
        
        ans = 0
        for num_places in range(1, self.N):
            ans += self.D ** num_places
        ans += self.helper(0)
        return ans
    
    def helper(self, idx):
        if idx > self.N - 1:
            return 1
        
        ans = 0
        num_digits_left = self.N - idx - 1
        ith_n = self.nlist[idx]
        for digit in self.digits:
            if digit < ith_n:
                ans += self.D ** num_digits_left
            elif digit == ith_n:
                ans += self.helper(idx+1)
            else:
                pass
        return ans