# 84. Largest Rectangle in Histogram
# Hard

# 4935

# 103

# Add to List

# Share
# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


# The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

# Example:

# Input: [2,1,5,6,2,3]
# Output: 10


# This solution works !

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        for each hight, we find the max area by only including the buildings that are taller than or equal to yourself
        '''
        
        # 1 keep track of the left most (smaller than you) using stack for each element
        stack = []
        left = [0 for _ in range(len(heights))]
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = 0 if not stack else stack[-1] +1
            stack.append(i)
        
        # 2 keep track of the right most (smaller than you) using stack for each element
        stack = []
        right = [0 for _ in range(len(heights))]
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = len(heights)-1 if not stack else stack[-1] -1
            stack.append(i)
        
        # 3 get the max area
        best = 0
        for i in range(len(left)):
            best = max(best, ((right[i] - left[i] +1 ) * heights[i]))
        return best        
    
