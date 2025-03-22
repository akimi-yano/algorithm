'''
2685. Count the Number of Complete Components
Medium
Topics
Companies
Hint
You are given an integer n. There is an undirected graph with n vertices, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting vertices ai and bi.

Return the number of complete connected components of the graph.

A connected component is a subgraph of a graph in which there exists a path between any two vertices, and no vertex of the subgraph shares an edge with a vertex outside of the subgraph.

A connected component is said to be complete if there exists an edge between every pair of its vertices.

 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4]]
Output: 3
Explanation: From the picture above, one can see that all of the components of this graph are complete.
Example 2:



Input: n = 6, edges = [[0,1],[0,2],[1,2],[3,4],[3,5]]
Output: 1
Explanation: The component containing vertices 0, 1, and 2 is complete since there is an edge between every pair of two vertices. On the other hand, the component containing vertices 3, 4, and 5 is not complete since there is no edge between vertices 4 and 5. Thus, the number of complete components in this graph is 1.
 

Constraints:

1 <= n <= 50
0 <= edges.length <= n * (n - 1) / 2
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no repeated edges.
'''

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        1) find the connected components -> union find
        2) count the number of edges
        3) calculate the expected number of edges : (V * V-1) / 2
        4) check if we have the expected number of edges
        '''
        parent = list(range(n)) # [0, 1, 2, 3, 4, 5]
        rank = [0] * (n) # [0, 0, 0, 0, 0, 0]

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1
            
        for u, v in edges: 
            union(u, v)
        
        component_vertices = {}
        component_edges = {}
        
        for node in range(n):
            root = find(node)
            if root not in component_vertices:
                component_vertices[root] = set()
                component_edges[root] = 0
            component_vertices[root].add(node)
        
        for u, _ in edges:
            root = find(u)
            component_edges[root] += 1
        
        complete_count = 0
        for root in component_vertices:
            num_vertices = len(component_vertices[root])
            expected_num_edges = (num_vertices * (num_vertices -1)) // 2

            if component_edges[root] == expected_num_edges:
                complete_count += 1
        
        return complete_count