# 1791. Find Center of Star Graph
# Medium

# 11

# 11

# Add to List

# Share
# There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

# You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

 

# Example 1:


# Input: edges = [[1,2],[2,3],[4,2]]
# Output: 2
# Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.
# Example 2:

# Input: edges = [[1,2],[5,1],[1,3],[1,4]]
# Output: 1
 

# Constraints:

# 3 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 1 <= ui, vi <= n
# ui != vi
# The given edges represent a valid star graph.

# This solution works:

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        memo = {}
        for node1, node2 in edges:
            if node1 not in memo:
                memo[node1] = 0
            if node2 not in memo:
                memo[node2] = 0
            memo[node1] += 1
            memo[node2] += 1
        
        maxcount = 0
        maxval = None
        for k, v in memo.items():
            if v > maxcount:
                maxcount = v
                maxval = k
        return maxval
            
                
