# 218. The Skyline Problem
# Hard

# 2548

# 144

# Add to List

# Share
# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.

# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:

# lefti is the x coordinate of the left edge of the ith building.
# righti is the x coordinate of the right edge of the ith building.
# heighti is the height of the ith building.
# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

# The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate  0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]

 

# Example 1:


# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points in the output list.
# Example 2:

# Input: buildings = [[0,2,3],[2,5,3]]
# Output: [[0,3],[5,0]]
 

# Constraints:

# 1 <= buildings.length <= 104
# 0 <= lefti < righti <= 231 - 1
# 1 <= heighti <= 231 - 1
# buildings is sorted by lefti in non-decreasing order.


# This solution works:
    
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # Use an infinite vertical line x to scan from left to right. If max height changes, record [x, height] in res. Online judge is using Python 2.7.9 and there's no max heap's push and pop method, so we can use a min heap hp storing -H as "max heap". Thanks to this discussion, set comprehension is faster and shorter than list(set((R, 0, None) for L, R, H in buildings)).
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]: 
                heapq.heappop(hp)
            if negH: 
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]: 
                res += [x, -hp[0][0]],
        return res[1:]

# This solution works:

from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        
        events = []
        for l, r, h in buildings:
            events.append((l, -h, 0))
            events.append((r, h, 1))
            
        events.sort()
        
        ans = []
        active_heights = SortedList([0])
        n = len(events)
        i = 0
        while i < n:
            x,h,t = events[i]
            if t == 0:
                active_heights.add(-h)
            else:
                active_heights.remove(h)
            i += 1
            
            # check if the biggest height has changed
            if not ans or ans[-1][1] != active_heights[-1]:
                ans.append((x, active_heights[-1]))
        return ans
        