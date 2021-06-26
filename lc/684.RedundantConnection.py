# 684. Redundant Connection
# Medium

# 2499

# 264

# Add to List

# Share
# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

# Example 1:


# Input: edges = [[1,2],[1,3],[2,3]]
# Output: [2,3]
# Example 2:


# Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
# Output: [1,4]
 

# Constraints:

# n == edges.length
# 3 <= n <= 1000
# edges[i].length == 2
# 1 <= ai < bi <= edges.length
# ai != bi
# There are no repeated edges.
# The given graph is connected.

# This solution works:

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        def find(x):
            if x == roots[x-1]:
                return x
            roots[x-1] = find(roots[x-1])
            return roots[x-1]
        
        def union(x, y):
            x = find(x)
            y = find(y)
            if x == y:
                return True
            else:
                if x < y:
                    roots[x-1] = y
                else:
                    roots[y-1] = x
                return False
        
        all_nodes = set([])
        for x, y in edges:
            all_nodes.add(y)
            all_nodes.add(x)
        N = len(all_nodes) 
        roots = [num for num in range(1, N+1)]
        ans = []
        for x, y in edges:
            if union(x,y):
                ans = [x,y] 
        return ans