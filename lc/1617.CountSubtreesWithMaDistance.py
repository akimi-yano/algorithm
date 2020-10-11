# 1617. Count Subtrees With Max Distance Between Cities
# Hard

# 16

# 7

# Add to List

# Share
# There are n cities numbered from 1 to n. You are given an array edges of size n-1, where edges[i] = [ui, vi] represents a bidirectional edge between cities ui and vi. There exists a unique path between each pair of cities. In other words, the cities form a tree.

# A subtree is a subset of cities where every city is reachable from every other city in the subset, where the path between each pair passes through only the cities from the subset. Two subtrees are different if there is a city in one subtree that is not present in the other.

# For each d from 1 to n-1, find the number of subtrees in which the maximum distance between any two cities in the subtree is equal to d.

# Return an array of size n-1 where the dth element (1-indexed) is the number of subtrees in which the maximum distance between any two cities is equal to d.

# Notice that the distance between the two cities is the number of edges in the path between them.

 

# Example 1:



# Input: n = 4, edges = [[1,2],[2,3],[2,4]]
# Output: [3,4,0]
# Explanation:
# The subtrees with subsets {1,2}, {2,3} and {2,4} have a max distance of 1.
# The subtrees with subsets {1,2,3}, {1,2,4}, {2,3,4} and {1,2,3,4} have a max distance of 2.
# No subtree has two nodes where the max distance between them is 3.
# Example 2:

# Input: n = 2, edges = [[1,2]]
# Output: [1]
# Example 3:

# Input: n = 3, edges = [[1,2],[2,3]]
# Output: [2,1]
 

# Constraints:

# 2 <= n <= 15
# edges.length == n-1
# edges[i].length == 2
# 1 <= ui, vi <= n
# All pairs (ui, vi) are distinct.


# # This approach does not work: 
# class Solution:
#     def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
#         '''
#         [3,4,0]
#         size = n-1
#         max_distance = 1: there are 3 subtrees {}
#         max_distance = 2: there are 4 subtrees
#         max_distance = 3: there are 0 subtrees
#         '''
        
#         ans = [{} for _ in range(n-1)]
        
#         adj_list = {}
        
#         for n1, n2, in edges:
#             if n1 not in adj_list:
#                 adj_list[n1] = []
#             adj_list[n1].append(n2)
            
#             if n2 not in adj_list:
#                 adj_list[n2] = []
#             adj_list[n2].append(n1)
            
#         def helper(cur):
#             pass
        
        
        
#         return [len(elem) for elem in ans]


'''
1 list out all the combinations
2 check if they are connected
3 traverse DFS to get max depth /distance of each tree - use set for every traverse
4 update the answer arr
'''

# This solution works !

class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        # make the adjacency list. Each node is represented by a single bit.
        self.adj = {1 << node: set([]) for node in range(n)}
        for n1, n2 in edges:
            n1 = 1 << (n1 - 1)
            n2 = 1 << (n2 - 1)
            self.adj[n1].add(n2)
            self.adj[n2].add(n1)

        self.N = 1 << n
        ans = [0 for _ in range(n-1)]
        for subtree in range(3, self.N):
            if not self.connected(subtree):
                continue
            max_len = 0
            for node in self.adj:
                max_len = max(max_len, self.helper(subtree, node, 0))
            if max_len < 2:
                continue
            ans[max_len - 1 - 1] += 1
        return ans
    
    # DFS, return max depth
    def helper(self, subtree, node, seen):
        if seen & node or not subtree & node:
            return 0
        ans = 0
        seen |= node
        for next_node in self.adj[node]:
            ans = max(ans, self.helper(subtree, next_node, seen))
        seen ^= node
        return ans + 1
    
    # BFS, return True if subtree is connected else False
    def connected(self, subtree):
        first_node = 1
        
        # print('finding first node in subtree {}'.format(bin(subtree)))
        while not subtree & first_node:
            first_node <<= 1
        # print('found first node! {}'.format(bin(first_node)))

        seen = 0
        queue = deque([first_node])
        while len(queue) > 0:
            node = queue.popleft()
            # skip if the node has been visited, or it's not part of the subtree
            if seen & node or not subtree & node:
                continue
            seen |= node
            for next_node in self.adj[node]:
                queue.append(next_node)

        return subtree == seen