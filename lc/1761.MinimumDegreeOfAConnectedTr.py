# 1761. Minimum Degree of a Connected Trio in a Graph
# Hard

# 14

# 41

# Add to List

# Share
# You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

# A connected trio is a set of three nodes where there is an edge between every pair of them.

# The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

# Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.

 

# Example 1:


# Input: n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
# Output: 3
# Explanation: There is exactly one trio, which is [1,2,3]. The edges that form its degree are bolded in the figure above.
# Example 2:


# Input: n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
# Output: 0
# Explanation: There are exactly three trios:
# 1) [1,4,3] with degree 0.
# 2) [2,5,6] with degree 2.
# 3) [5,6,7] with degree 2.
 

# Constraints:

# 2 <= n <= 400
# edges[i].length == 2
# 1 <= edges.length <= n * (n-1) / 2
# 1 <= ui, vi <= n
# ui != vi
# There are no repeated edges.


'''
overwhelmed by diagram
write down what I need to do in steps

with the data I have, try to organize it and write down to think how I can use the information I have (visualize)
draw out the adjecency list
'''

# This solution works:

class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: set([]) for i in range(1, n+1)}
        for n1, n2 in edges:
            adj[n1].add(n2)
            adj[n2].add(n1)
            
        best = float('inf')
        for n1, neighbors in adj.items():
            for n2 in neighbors:
                if n2 <= n1:
                    continue
                for n3 in neighbors:
                    if n3 <= n2:
                        continue
                    if n3 in adj[n2]:
                        best = min(best, len(adj[n1]) + len(adj[n2]) + len(adj[n3]) - 6)
        if best == float('inf'):
            return -1
        return best