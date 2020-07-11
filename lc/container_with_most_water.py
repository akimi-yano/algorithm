# https://leetcode.com/problems/container-with-most-water/
def maxArea(height):
  left = 0
  right = len(height)-1
  
  
  distance = len(height) - 1
  max_area = distance * min(height[left],height[right])
  while left < right:
    distance -= 1
    moving_left = abs(height[left] - height[left + 1])
    moving_right = abs(height[right] - height[right - 1])
    if moving_left >= moving_right:
      left = left+1
    else:
      right = right-1
    max_area = max(max_area, distance * min(height[left], height[right]))
  return max_area
print(maxArea([1,8,6,2,5,4,8,3,7])) #49
print(maxArea([1,3,2,5,25,24,5])) #21

