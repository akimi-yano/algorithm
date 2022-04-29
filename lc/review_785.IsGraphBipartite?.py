# 785. Is Graph Bipartite?
# Medium

# 4109

# 263

# Add to List

# Share
# There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
# A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph connects a node in set A and a node in set B.

# Return true if and only if it is bipartite.

 

# Example 1:


# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in one and a node in the other.
# Example 2:


# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
 

# Constraints:

# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.


# This solution works:


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        memo = {}
        def helper(cur, group):
            if cur in memo:
                return memo[cur] == group
            memo[cur] = group
            for next_node in graph[cur]:
                if not helper(next_node, group^1):
                    return False
            return True
        
        for i in range(len(graph)):
            if i not in memo:
                ans = helper(i, 0)
                if ans is False:
                    return False
        return True
    
    '''
    [[1,3],[0,2],[1,3],[0,2]]
    cur
    {0:0}
    
    0 - 4 - 2 
        |
        3
    1
    '''
    '''
    [[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]
    0
    
    6 - 1 - 2
        |
        4
        
    1 - 2 - 4
        ||
        89
        
    7 - 3 - 8
    
    2 - 4 - 1
        ||
        89
    '''