'''
1857. Largest Color Value in a Directed Graph
Hard
Topics
Companies
Hint
There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n
'''

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        graph = {}
        indeg = [0] * len(colors)
        for u, v in edges: 
            indeg[v] += 1
            graph.setdefault(u, []).append(v)
            
        # Kahn's algo
        roots = [x for x in range(len(colors)) if indeg[x] == 0]
        
        stack = roots.copy()
        nodes = []
        while stack: 
            x = stack.pop()
            nodes.append(x)
            for xx in graph.get(x, []):
                indeg[xx] -= 1
                if indeg[xx] == 0: stack.append(xx)
        if len(nodes) < len(colors): return -1 # cycle detected 
        
        @cache
        def fn(x): 
            """Return distribution of (maximized) colors at given node."""
            ans = [0]*26
            ans[ord(colors[x]) - 97] = 1
            for xx in graph.get(x, []): 
                val = fn(xx)
                for i in range(26): 
                    if i == ord(colors[x]) - 97: ans[i] = max(ans[i], 1 + val[i])
                    else: ans[i] = max(ans[i], val[i])
            return ans 
        
        ans = [0]*26 
        for root in roots: 
            val = fn(root)
            for i in range(26): ans[i] = max(ans[i], val[i])
        return max(ans)