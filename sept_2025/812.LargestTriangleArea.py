'''
812. Largest Triangle Area
Solved
Easy
Topics
premium lock icon
Companies
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
Example 2:

Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
 

Constraints:

3 <= points.length <= 50
-50 <= xi, yi <= 50
All the given points are unique.
'''

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        '''
        area of triangle ABC = 1/2 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1)
        '''
        max_area = 0
        for a, b, c in itertools.combinations(points, 3):
            x1, y1 = a
            x2, y2 = b
            x3, y3 = c
            max_area = max(max_area, (1/2 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1)))
        return max_area