# 1719. Number Of Ways To Reconstruct A Tree
# Hard

# 21

# 11

# Add to List

# Share
# You are given an array pairs, where pairs[i] = [xi, yi], and:

# There are no duplicates.
# xi < yi
# Let ways be the number of rooted trees that satisfy the following conditions:

# The tree consists of nodes whose values appeared in pairs.
# A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is an ancestor of xi.
# Note: the tree does not have to be a binary tree.
# Two ways are considered to be different if there is at least one node that has different parents in both ways.

# Return:

# 0 if ways == 0
# 1 if ways == 1
# 2 if ways > 1
# A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

# An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.


# Example 1:


# Input: pairs = [[1,2],[2,3]]
# Output: 1
# Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
# Example 2:


# Input: pairs = [[1,2],[2,3],[1,3]]
# Output: 2
# Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
# Example 3:

# Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
# Output: 0
# Explanation: There are no valid rooted trees.


# Constraints:

# 1 <= pairs.length <= 105
# 1 <= xi < yi <= 500
# The elements in pairs are unique.

# This solution works !!!!
'''
1 First, create graph from our pairs array.
2 Function helper(nodes) have input set of nodes and try to solve subproblem with this set.
3 We discussed, that we need to find node which is connected with all other nodes, 
that is its degree should be equal to m = len(nodes) - 1.
4 If we did not found such a node, we can immedietly return 0: it is not possible to recunstruct a tree.
5 If there is such a node, let us denote it root. Actually, 
it can happen that there is more than one node with this property and in this case any of them 
can be root and if we have say U possible solution with first of them being root, 
that there will be exactly U possible solutions if another will be root - we can just replace one of them with another.
6 Now, we clean our graph g: we remove all connections between root and all its neighbours 
(actually it is enough to cut only one way connections)
7 Next step is to perform dfs to find connected components.
8 Finally, we run our helper function on each of found components: if it happens that for some subproblem we have answer 0, 
it means that for original problem we also need to return 0. 
If 0 not here and we met 2 in our cands, than we return 2: it means, 
that we found 2 or more solutions for some subproblems and 1 for others, 
like cands = [1, 2, 1, 1, 2]. In this case, we can be sure, that we have more than 2 solutions (in fact we have 1*2*1*1*2). 
Finally, important point: if we have len(d[m]) >= 2, we also return 2 - see step 5.
'''
class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        # made adj list with set 
        adj = {}
        for n1, n2 in pairs:
            if n1 not in adj:
                adj[n1] = set([])
            if n2 not in adj:
                adj[n2] = set([])
            adj[n1].add(n2)
            adj[n2].add(n1)
        
        # dfs to add node into group set
        def dfs(seen, group, node):
            if node in seen:
                return
            seen.add(node)
            group.add(node)
            for nxt in adj[node]:
                dfs(seen, group, nxt)
    
        def helper(nodes):
            # if the nodes number is 0 or 1, there are only 1 option each - 0 graph or 1 graph
            if len(nodes) < 2:
                return 1
            
            # check if there is any root if so how many - if no root, return 0
            root = None
            num_roots = 0
            for node in nodes:
                if len(adj[node]) == len(nodes) - 1:
                    root = node
                    num_roots += 1
            if root is None:
                return 0
            
            # remove root from adjacency list
            nodes.remove(root)
            for node in nodes:
                adj[node].remove(root)

            # separate nodes into different groups
            groups = []
            seen = set([])
            for node in nodes:
                if node not in seen:
                    group = set([])
                    dfs(seen, group, node)
                    groups.append(group)
            
            # if there is any group_ans == 0 then its 0
            # check if ans is larger then 1 or number of choices of roots is more than 1 then return 2
            # otherwise return 1
            ans = 0
            for group in groups:
                group_ans = helper(group)
                if group_ans == 0:
                    return 0
                ans = max(ans, group_ans)
            if ans > 1 or num_roots > 1:
                return 2
            return 1

        return helper(set(adj.keys()))
        