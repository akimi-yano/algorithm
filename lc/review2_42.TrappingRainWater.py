# 42. Trapping Rain Water
# Hard

# 22245

# 298

# Add to List

# Share
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9
 

# Constraints:

# n == height.length
# 1 <= n <= 2 * 104
# 0 <= height[i] <= 105


# This solution works:


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        for each height, keep track of the heighest on its left side and right side by checking
        from left and right and get the min of both, from there subtract the current height to keep 
        accumulating the ans
        '''
        highest_on_left = [0 for _ in range(len(height))]
        highest_on_right = [0 for _ in range(len(height))]
        
        highest = 0
        for i in range(len(height)):
            highest = max(highest, height[i])
            highest_on_left[i] = highest
        
        highest = 0
        for i in range(len(height)-1,-1,-1):
            highest = max(highest, height[i])
            highest_on_right[i] = highest
        
        ans = 0
        for i in range(len(height)): 
            min_of_heighest_sides = min(highest_on_right[i], highest_on_left[i])
            ans += (min_of_heighest_sides - height[i])
        return ans