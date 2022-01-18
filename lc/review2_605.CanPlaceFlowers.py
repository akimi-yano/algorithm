# 605. Can Place Flowers
# Easy

# 2281

# 578

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


# This solution works:


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1 and flowerbed[0] == 0:
            return n <= 1
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            elif i == 0:
                if i+1 < len(flowerbed) and flowerbed[i+1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            elif i == len(flowerbed)-1:
                if i-1 > -1 and flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    n -= 1
            else:
                 if i+1 < len(flowerbed) and flowerbed[i+1] != 1 and i-1 > -1 and flowerbed[i-1] != 1:
                    flowerbed[i] = 1
                    n -= 1
   
        return n <= 0