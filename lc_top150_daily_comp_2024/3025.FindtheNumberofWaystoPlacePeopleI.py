'''
3025. Find the Number of Ways to Place People I
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D array points of size n x 2 representing integer coordinates of some points on a 2D plane, where points[i] = [xi, yi].

Count the number of pairs of points (A, B), where

A is on the upper left side of B, and
there are no other points in the rectangle (or line) they make (including the border).
Return the count.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]

Output: 0

Explanation:



There is no way to choose A and B so A is on the upper left side of B.

Example 2:

Input: points = [[6,2],[4,4],[2,6]]

Output: 2

Explanation:



The left one is the pair (points[1], points[0]), where points[1] is on the upper left side of points[0] and the rectangle is empty.
The middle one is the pair (points[2], points[1]), same as the left one it is a valid pair.
The right one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0], but points[1] is inside the rectangle so it's not a valid pair.
Example 3:

Input: points = [[3,1],[1,3],[1,1]]

Output: 2

Explanation:



The left one is the pair (points[2], points[0]), where points[2] is on the upper left side of points[0] and there are no other points on the line they form. Note that it is a valid state when the two points form a line.
The middle one is the pair (points[1], points[2]), it is a valid pair same as the left one.
The right one is the pair (points[1], points[0]), it is not a valid pair as points[2] is on the border of the rectangle.
 

Constraints:

2 <= n <= 50
points[i].length == 2
0 <= points[i][0], points[i][1] <= 50
All points[i] are distinct.
'''

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        # Step 1: Sort points by x ascending, then by y descending
        points.sort(key=lambda x: (x[0], -x[1]))
        pair_count = 0
        n = len(points)
        # Step 2: Iterate through all points as potential "upper-left" points
        for i in range(n):
            upper_y = points[i][1]
            lower_y_limit = float('-inf')
            # Step 3: Check subsequent points as potential "bottom-right" points
            for j in range(i + 1, n):
                current_y = points[j][1]
                if current_y <= upper_y and current_y > lower_y_limit:
                    pair_count += 1
                    lower_y_limit = current_y
                    if current_y == upper_y:
                        break
        return pair_count