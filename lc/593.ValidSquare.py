# 593. Valid Square
# Medium

# 376

# 530

# Add to List

# Share
# Given the coordinates of four points in 2D space, return whether the four points could construct a square.

# The coordinate (x,y) of a point is represented by an integer array with two integers.

# Example:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: True


# Note:

# All the input integers are in the range [-10000, 10000].
# A valid square has four equal sides with positive length and four equal angles (90-degree angles).
# Input points have no order.



# This approach does not work !
# class Solution:
#     def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
#         arr = [p1,p2,p3,p4]
#         arr.sort()
        
#         sx, sy = arr[0]
#         lx, ly = arr[len(arr)-1]
#         x1, y1 = arr[1]
#         x2, y2 = arr[2]
        
#         return (lx-x1)**2 + (ly-y1)**2 == (lx-x2)**2 + (ly-y2)**2 ==  (sx-x1)**2 + (sy-y1)**2 == (sx-x2)**2 + (sy-y2)**2

'''
        edge case 
        
        [1,1]
        [5,3]
        [3,5]
        [7,7]
        
        7       @
        5   @
        3     @
        1 @   
          1 3 5 7  
'''

# This solution works !

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = set([tuple(p) for p in [p1, p2, p3, p4]])
        p12 = abs(p1[0]-p2[0])**2 + abs(p1[1]-p2[1])**2
        p13 = abs(p1[0]-p3[0])**2 + abs(p1[1]-p3[1])**2
        p14 = abs(p1[0]-p4[0])**2 + abs(p1[1]-p4[1])**2
        side, diag = min(p12, p13, p14), max(p12, p13, p14)

        for x in points:
            sidecnt = diagcnt = 0
            others = points - set([x])
            for y in others:
                dist = abs(x[0]-y[0])**2 + abs(x[1]-y[1])**2
                if dist == side:
                    sidecnt += 1
                elif dist == diag:
                    diagcnt += 1
            if sidecnt != 2 or diagcnt != 1:
                return False
        return True