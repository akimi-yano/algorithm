# 149. Max Points on a Line

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Example 1:

# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
# Example 2:

# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.




class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # because of floating point precision errors/overflow, we should keep
        # the slope and intercept in their frational terms.

        if len(points)==0:
            return 0
        
        # keep track of unique points and their counts
        unique_points = {}
        for p in points:
            x, y = p[0], p[1]
            if (x, y) not in unique_points:
                unique_points[(x, y)] = 1
            else:
                unique_points[(x, y)] += 1
        
        # if there is only one unique point, then we can't make lines.
        # just return its count.
        if len(unique_points)==1:
            return max(unique_points.values())

        # make a dictionary of unique equations
        equations = {}
        def helper(p1,p2):
            x1,y1=p1
            x2,y2=p2
            a = (y2-y1, x2-x1)
            b = (a[1]*y1-a[0]*x1, a[1])
            # if the denominator of the slope is zero, we have a perpendicular line.
            # this is defined by the x value.
            if a[1] == 0:
                a = float('inf')
                b = x1
            # otherwise, we have a normal line.
            else:
                # reduce the numerator and denominator by their GCD.
                a_gcd = math.gcd(a[0], a[1])
                a = a[0]//a_gcd, a[1]//a_gcd
                # same for the intercept (seppen).
                b_gcd = math.gcd(b[0], b[1])
                b = b[0]//b_gcd, b[1]//b_gcd
            # add the points to the equation's set.
            if (a, b) not in equations:
                equations[a, b] = set([])
            equations[(a, b)].add(tuple(p1))
            equations[(a, b)].add(tuple(p2))
        
        # calculate all unique equations.
        for p1 in unique_points:
            for p2 in unique_points:
                if p1 == p2:
                    continue
                helper(p1, p2)
        
        # print(equations)
        best = 0
        for equation, pts in equations.items():
            # tally up the unique points count, and update best as necessary.
            best = max(best, sum([unique_points[pt] for pt in pts]))
        return best
            
            
            
            