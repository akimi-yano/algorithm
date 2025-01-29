'''
684. Redundant Connection
Medium
Topics
Companies
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
'''

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {v: -1 for v in range(1, len(edges)+1)}

        def find(u):
            # find root with path compression
            if parent[u] != -1:
                parent[u] = find(parent[u])
                return parent[u]
            # root node must be with -1
            else:   
                return u
        
        def union(u, v):
            parent_of_u = find(u)
            parent_of_v = find(v)

            # u and v has the same parent node
            # this edges forms a cycle in graph
            if parent_of_u == parent_of_v:    
                return True
            # after adding edge (u, v)
            # graph is still a tree without cycle
            else:
                parent[parent_of_u] = parent_of_v
                return False
        
        for u, v in edges:
            # check if edge (u, v) forms a cycle
            if union(u, v):
                return [u, v]
        