# 1857. Largest Color Value in a Directed Graph
# Hard

# 155

# 7

# Add to List

# Share
# There is a directed graph of n colored nodes and m edges. The nodes are numbered from 0 to n - 1.

# You are given a string colors where colors[i] is a lowercase English letter representing the color of the ith node in this graph (0-indexed). You are also given a 2D array edges where edges[j] = [aj, bj] indicates that there is a directed edge from node aj to node bj.

# A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color value of the path is the number of nodes that are colored the most frequently occurring color along that path.

# Return the largest color value of any valid path in the given graph, or -1 if the graph contains a cycle.

 

# Example 1:



# Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
# Output: 3
# Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
# Example 2:



# Input: colors = "a", edges = [[0,0]]
# Output: -1
# Explanation: There is a cycle from 0 to 0.
 

# Constraints:

# n == colors.length
# m == edges.length
# 1 <= n <= 105
# 0 <= m <= 105
# colors consists of lowercase English letters.
# 0 <= aj, bj < n

# This solution works:

'''
cycle detection using three colors
'''

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        @lru_cache(None)
        def helper(node, color):
            nonlocal adj, colors
            cur_val = 1 if colors[node] == color else 0
            if not adj[node]:
                return cur_val
            return cur_val + max(helper(nxt, color) for nxt in adj[node])
        
        # gray mean visiting and not sure if there is cycle
        def cycle(node, GRAY):
            nonlocal adj, WHITE, BLACK
            if node in GRAY:
                return True
            WHITE.remove(node)
            GRAY.add(node)
            for nxt in adj[node]:
                if nxt not in BLACK and cycle(nxt, GRAY):
                    return True
            BLACK.add(node)
            GRAY.remove(node)
            return False

        N = len(colors)
        # white means not visited
        WHITE = set(range(N))
        # black means visited and confirmed no cycle
        BLACK = set([])
        
        adj = {node: set([]) for node in range(N)}
        for start_node, end_node in edges:
            adj[start_node].add(end_node)
        
        while WHITE:
            start_node = next(iter(WHITE))
            if cycle(start_node, set([])):
                return -1

        best = 0
        colorset = set(colors)
        for color in colorset:
            for start_node in range(N):
                best = max(best, helper(start_node, color))
        return best
