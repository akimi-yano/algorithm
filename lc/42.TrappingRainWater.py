# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

# Example:

# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

class Solution:
    def trap(self, height: List[int]) -> int:
        # handle an edge case: the arr is empty
        if len(height) == 0:
            return 0
        
        # prepopulate the left max arr - iterate forwards
        n = len(height)
        left_max = [0]*n
        left_max[0] = height[0]
        for i in range(1,n):
            left_max[i] = max(left_max[i-1],height[i])
            
        # prepopulate the right max arr - iterate backwards
        right_max = [0]*n
        right_max[n-1]=height[n-1]
        for k in range(n-2,-1,-1):
            right_max[k] = max(height[k],right_max[k+1])
            
        # just get the min of the left_max and right_max and subtract its self 
        # and add to total
        total_water = 0
        for j in range(1,n):
            water_and_building = min(left_max[j],right_max[j])
            water = water_and_building - height[j]
            total_water+=water
        return total_water