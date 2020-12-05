# 605. Can Place Flowers
# Easy

# 1119

# 406

# Add to List

# Share
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:

# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: true
# Example 2:

# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: false
 

# Constraints:

# 1 <= flowerbed.length <= 2 * 104
# flowerbed[i] is 0 or 1.
# There are no two adjacent flowers in flowerbed.
# 0 <= n <= flowerbed.length

# this approach does not work - TLE 

# class Solution:
#     def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
#         def helper(i, canplace, remaining):
#             key = (i, canplace, remaining)
#             if key in memo:
#                 return memo[key]
            
#             ans = False
            
#             if i > len(flowerbed) -1:
#                 if remaining <= 0:
#                     ans |= True
#                 else:
#                     pass
            
#             elif flowerbed[i]:
#                 if not canplace:
#                     pass
#                 else:
#                     ans |= helper(i+1, False, remaining)
#             else:
#                 if canplace:
#                     flowerbed[i] = 1
#                     ans |= helper(i+1, False, remaining -1)
#                     flowerbed[i] = 0
#                 ans |= helper(i+1, True, remaining)
#             memo[key] = ans
#             return ans
#         memo = {}
#         return helper(0, True, n)
                
                
                
# This solution works - find pattern and make a math  formula

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # if there are no flowers
        if not sum(flowerbed):
            return (len(flowerbed)+1) // 2 >= n
        
        ans = 0
        prev = -2
        for i, has_flower in enumerate(flowerbed):
            if has_flower:
                ans += (i-prev-2) // 2
                prev = i

        ans += (len(flowerbed)-prev-1) // 2
        return ans >= n