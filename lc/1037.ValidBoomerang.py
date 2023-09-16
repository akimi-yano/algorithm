'''
1037. Valid Boomerang
Easy
376
502
Companies
Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

 

Example 1:

Input: points = [[1,1],[2,3],[3,2]]
Output: true
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: false
 

Constraints:

points.length == 3
points[i].length == 2
0 <= xi, yi <= 100
'''


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        '''
        0    1    2    3

        1    @

        2              @

        3          @
        '''
        '''
        Approach: get triangle's area -> the area is not zero: because if all of these points are on the same straight line, then the triangle will have have an area of 0
        The formula is:
        | (Ax * (By − Cy) + Bx * (Cy − Ay) + Cx * (Ay − By)) / 2 |
        '''
        Ax, Ay = points[0]
        Bx, By = points[1]
        Cx, Cy = points[2]

        area = abs(((Ax*(By-Cy))+(Bx*(Cy-Ay))+(Cx*(Ay-By)))/2)
        return area != 0


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        '''
        Approach: compare the slopish thing of 2 angles (just 2 is enough)
        avoid dividing, just compare a/b and c/d if(a * d > c * b)==> first fraction is greater otherwise second
        '''
        Ax, Ay = points[0]
        Bx, By = points[1]
        Cx, Cy = points[2]

        # (Ay-By)/(Ax-Bx) = (Cy-By)/(Cx-Bx) 
        return (Ay-By) * (Cx-Bx) != (Ax-Bx) * (Cy-By)