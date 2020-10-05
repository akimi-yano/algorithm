# 1610. Maximum Number of Visible Points
# Medium

# 6

# 44

# Add to List

# Share
# You are given an array points, an integer angle, and your location, where location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

# Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In other words, posx and posy cannot be changed. Your field of view in degrees is represented by angle, determining how wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].


# You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east direction from your position is in your field of view.

# There can be multiple points at one coordinate. There may be points at your location, and you can always see these points regardless of your rotation. Points do not obstruct your vision to other points.

# Return the maximum number of points you can see.



# Example 1:


# Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
# Output: 3
# Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
# Example 2:

# Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
# Output: 4
# Explanation: All points can be made visible in your field of view, including the one at your location.
# Example 3:


# Input: points = [[0,1],[2,1]], angle = 13, location = [1,1]
# Output: 1
# Explanation: You can only see one of the two points, as shown above.


# Constraints:

# 1 <= points.length <= 105
# points[i].length == 2
# location.length == 2
# 0 <= angle < 360
# 0 <= posx, posy, xi, yi <= 109


# This solution works!:
'''
1 convert all coordinates to radians and append them to an array
2 sort the array
3 sliding window to find the longest window that satisfies arr[r] - arr[l] <= angle.

'''
import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        '''
        math.atan2(dy,dx) 
        this returns an radian by passing in dy and dx which is delta (henka) 
        of each point relative to the location of the person
        '''
        lx, ly = location
        angles = []
        same_points = 0
        for px, py in points:
            dy, dx = py - ly, px - lx
            if dx == 0 and dy == 0:
                same_points += 1
                continue
            deg = math.atan2(dy, dx) * 180 / math.pi
            
            # This is only necessary only of we'll have other cordinations rather than x, y being both positive:
            
            # if deg < 0:
            #     if dx < 0 :
            #         deg += 180
            #     else:
            #         deg += 360
            # else:
            #     if dx < 0 or dy < 0:
            #         deg += 180
                
            angles.append(deg)
            
        angles.sort()
        angles2 = [deg + 360 for deg in angles]
        all_degs = angles + angles2
        
        left = best = 0
        for right in range(len(all_degs)):
            while all_degs[right] - all_degs[left] > angle:
                left += 1
            best = max(best, right - left + 1 + same_points)
        
        return best
        


# This solution works ! optimization and clearn up:
    
    import math
class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        '''
        math.atan2(dy, dx) 
        this returns an radian by passing in dy and dx which is delta (henka) 
        of each point relative to the location of the person
        
        degree = math.atan2(dy, dx) * 180 / math.pi
        
        arctan to find the degree of the triangle
        
        if dx == 0 and dy == 0 meaning that if the point is the same as the 
        location point, we increment the count and add at the end to the answer
        
        we want to also sort the angle array and also add an array that is a +360 version of angle array to double the length
        since it's a circle/cycle, we want to back to the beginning after getting to the end
        sliding window to count the overlap within the window of the input angle
        keep track of the length right - left + 1 same_points
        '''
        lx, ly = location
        angles = []
        same_points = 0
        for px, py in points:
            dy, dx = py - ly, px - lx
            if dx == 0 and dy == 0:
                same_points += 1
                continue
            deg = math.atan2(dy, dx) * 180 / math.pi
                
            angles.append(deg)
            
        angles.sort()
        angles2 = [deg + 360 for deg in angles]
        all_degs = angles + angles2
        
        left = best = 0
        for right in range(len(all_degs)):
            while all_degs[right] - all_degs[left] > angle:
                left += 1
            best = max(best, right - left + 1 + same_points)
        
        return best
        
        