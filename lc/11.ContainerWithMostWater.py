# 11. Container With Most Water

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example:

# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


# THIS SOLUTION WORKS !!! very insuitive: start with two pointers, left and right, from beginning and end of the array
# and since every turn, the distance gets smaller, we need to choose a higher heights, by moving the pointer of smaller height
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxwater = 0
        left = 0
        right = len(height)-1
        while left<right:
            maxwater = max(maxwater, (min(height[left],height[right]) * (right-left)))
            if height[left] < height[right]:
                left = left+1
            else: 
                right = right-1
        return maxwater
    

# Another solution that works!
# If height[L] < height[R], move L, else move R. Say height[0] < height[5], 
# area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them.
class Solution:
    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res