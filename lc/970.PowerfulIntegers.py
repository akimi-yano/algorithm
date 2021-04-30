# 970. Powerful Integers
# Medium

# 116

# 47

# Add to List

# Share
# Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal to bound.

# An integer is powerful if it can be represented as xi + yj for some integers i >= 0 and j >= 0.

# You may return the answer in any order. In your answer, each value should occur at most once.

 

# Example 1:

# Input: x = 2, y = 3, bound = 10
# Output: [2,3,4,5,7,9,10]
# Explanation:
# 2 = 20 + 30
# 3 = 21 + 30
# 4 = 20 + 31
# 5 = 21 + 31
# 7 = 22 + 31
# 9 = 23 + 30
# 10 = 20 + 32
# Example 2:

# Input: x = 3, y = 5, bound = 15
# Output: [2,4,6,8,10,14]
 

# Constraints:

# 1 <= x, y <= 100
# 0 <= bound <= 106

# This solution works:
'''
generate and check all possible powers of x and y, whose sum is smaller than bound. Be careful with case x = 1 or y = 1 to avoid infinite loop.
'''

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        x_arr = [1]
        while x_arr[-1] * x < bound and x > 1:
            x_arr.append(x_arr[-1] * x)
            
        y_arr = [1]
        while y_arr[-1] * y < bound and y > 1:
            y_arr.append(y_arr[-1] * y)
            
        return list({i + j for i, j in product(x_arr, y_arr) if i+j <= bound})