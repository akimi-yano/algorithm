# 1584. Min Cost to Connect All Points
# Medium

# 41

# 9

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
# Example 3:

# Input: points = [[0,0],[1,1],[1,0],[-1,1]]
# Output: 4
# Example 4:

# Input: points = [[-1000000,-1000000],[1000000,1000000]]
# Output: 4000000
# Example 5:

# Input: points = [[0,0]]
# Output: 0
 

# Constraints:

# 1 <= points.length <= 1000
# -106 <= xi, yi <= 106
# All pairs (xi, yi) are distinct.


# This solution does not work:

# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
#         '''
#         generate all the paths and with weights and dijkistra to get to all nodes
#         '''
#         if len(points)<2:
#             return 0
#         total = 0
#         connected = set([])
#         newpoints = sorted(points,key = lambda elem : (elem[0],elem[1]))
#         for i in range(len(newpoints)):
#             xi = newpoints[i][0]
#             yi = newpoints[i][1]
#             closest = float('inf')
#             for k in range(len(newpoints)):
#                 if k == i:
#                     continue 
#                 if tuple(newpoints[k]) in connected:
#                     continue
#                 xk = newpoints[k][0]
#                 yk = newpoints[k][1]
#                 newcost = abs(xi - xk) + abs(yi - yk)
#                 if closest > newcost:
#                     closest = newcost
#                     pair = newpoints[k]
#             if closest!=float('inf'):
#                 total +=closest
#                 connected.add(tuple(pair))
#             connected.add(tuple(newpoints[i]))
#         return total
    
# This solution does not work :

# import heapq
# class Solution:
#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
#         '''
#         generate all the paths and with weights and dijkistra to get to all nodes
#         '''
#         adj = {}
#         for i, ipoint in enumerate(points):
#             xi, yi = ipoint[0], ipoint[1]
#             for k, kpoint in enumerate(points):
#                 if i==k:
#                     continue
#                 xk, yk = kpoint[0], kpoint[1]
#                 cost = abs(xi-xk) + abs(yi-yk)
#                 if i not in adj:
#                     adj[i]=[]
#                 else:
#                     adj[i].append((k,cost))
#         print(adj)


# THIS SOLUTION WORKS !: 

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
                # use count for fast exit 
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
    
    
'''
All points are connected if there is exactly one simple path between any two points.
So first sort the edges by the distance - from smallest to largest
and then use Union Find to see if there is a cycle -> if not, add that edge ! incrementing the cost 
Do the fast exit - if you find all the edges needed (n-1) return ans 
Optimize by optimizing the Union Find !

'''