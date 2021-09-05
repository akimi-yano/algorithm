# 834. Sum of Distances in Tree
# Hard

# 1883

# 57

# Add to List

# Share
# There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

# You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

# Return an array answer of length n where answer[i] is the sum of the distances between the ith node in the tree and all other nodes.

 

# Example 1:


# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
# Example 2:


# Input: n = 1, edges = []
# Output: [0]
# Example 3:


# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
 

# Constraints:

# 1 <= n <= 3 * 104
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.


# This solution works:


class Solution:
    def sumOfDistancesInTree(self, N, edges):
        G = defaultdict(set)
        for i, j in edges:
            G[i].add(j)
            G[j].add(i)
        
        def dfs(node, parent, depth):
            ans = 1
            for neib in G[node]:
                if neib != parent:
                    ans += dfs(neib, node, depth + 1)
            weights[node] = ans
            depths[node] = depth
            return ans
        
        def dfs2(node, parent, w):
            ans[node] = w
            for neib in G[node]:
                if neib != parent:
                    dfs2(neib, node, w + N - 2*weights[neib])
        
        weights, depths, ans = [0]*N, [0]*N, [0]*N
        dfs(0, -1, 0)
        dfs2(0, -1, sum(depths))
        
        return ans
        '''
        Let us first create graph G from our edges. Let us also use two different dfs functions:

        dfs(node, parent, depth), where node is current node we are in, parent is parent of current node and depth is depth of node. This function is used to traverse tree and for each node find two values: depth of node (how far it is from root) and also weight of node: how many nodes in subtree with given node. For example, for tree [[0,1],[0,2],[2,3],[2,4],[2,5]] weights will be [6, 1, 4, 1, 1, 1].
        dfs2(node, parent, w), where node and parent current node and its parent and w in answer for current node. How we can find answer for neib if we already now answer for node? It is w + N - 2*weights[neib], because when we moved from node to neib not a lot changed: for weights[neib] number of nodes distanced increased by 1 and for N - weights[neib] number of nodes distances decreased by 1.
        Finally, we just run dfs2(0, -1, sum(depths)).

        Complexity
        Time and space complexity is O(n).
        '''
