# 1584. Min Cost to Connect All Points
# Medium

# 1657

# 51

# Add to List

# Share
# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

 

# Example 1:


# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20
# Explanation: 

# We can connect the points as shown above to get the minimum cost of 20.
# Notice that there is a unique path between every pair of points.
# Example 2:

# Input: points = [[3,12],[-2,5],[-4,1]]
# Output: 18
 

# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.


# This solution works:


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Big idea: Union find to detect cycles. Create all edges, sort by distance. Look at each edge and add it if it doesn't make a cycle. Return the total of the added edges.
        '''
        edges = []
        for i in range(len(points)):
            p1 = tuple(points[i])
            for j in range(i+1, len(points)):
                p2 = tuple(points[j])
                dist = abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])
                edges.append((dist, p1, p2))
        edges.sort()
        # print(edges)
        
        self.roots = {(x, y): (x, y) for x, y in points}
        self.ranks = {(x, y): 0 for x, y in points}
        # print(self.roots)
        
        ans = 0
        count = 0
        for edge in edges:
            dist, p1, p2 = edge
            if self.union(p1, p2):
                ans += dist
                count += 1
                if count >= len(points) - 1:
                    return ans
        return ans
    
    def union(self, p1, p2):
        p1_root, p2_root = self.find(p1), self.find(p2)
        if p1_root == p2_root:
            return False
        if self.ranks[p1_root] < self.ranks[p2_root]:
            self.roots[p1_root] = p2_root
        elif self.ranks[p1_root] > self.ranks[p2_root]:
            self.roots[p2_root] = p1_root
        else:
            # when its equal - choose whichever and update the ranks
            self.roots[p1_root] = p2_root
            self.ranks[p2_root] += 1
            
        return True
    
    def find(self, p):
        if p != self.roots[p]:
            self.roots[p] = self.find(self.roots[p])
        return self.roots[p]