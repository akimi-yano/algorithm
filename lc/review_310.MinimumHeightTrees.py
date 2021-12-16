# 310. Minimum Height Trees
# Medium

# 4086

# 165

# Add to List

# Share
# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words, any connected graph without simple cycles is a tree.

# Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

# Return a list of all MHTs' root labels. You can return the answer in any order.

# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

 

# Example 1:


# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
# Example 2:


# Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
# Output: [3,4]
# Example 3:

# Input: n = 1, edges = []
# Output: [0]
# Example 4:

# Input: n = 2, edges = [[0,1]]
# Output: [0,1]
 

# Constraints:

# 1 <= n <= 2 * 104
# edges.length == n - 1
# 0 <= ai, bi < n
# ai != bi
# All the pairs (ai, bi) are distinct.
# The given input is guaranteed to be a tree and there will be no repeated edges.


# This solution works:


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        the answer is only one or two nodes
        start with leaves and remove
        '''
        # edge case
        if n <= 2:
            return [i for i in range(n)]
        
        # make adj list
        adj = {}
        for n1, n2 in edges:
            if n1 not in adj:
                adj[n1] = set([])
            if n2 not in adj:
                adj[n2] = set([])
            adj[n1].add(n2)
            adj[n2].add(n1)
        
        # save the leaves to start with
        leaves = []
        for k, v in adj.items():
            if len(v) == 1:
                leaves.append(k)
                
        # BFS topological 
        remaining = n
        while remaining >2:
            new_leaves = []
            while leaves:
                node = leaves.pop()
                remaining -= len(adj[node])
                for neighbor in adj[node]:
                    adj[neighbor].remove(node)
                    if len(adj[neighbor]) == 1:
                        new_leaves.append(neighbor)
            # swap
            leaves = new_leaves
        return leaves       