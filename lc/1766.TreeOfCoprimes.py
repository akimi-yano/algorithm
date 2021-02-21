# 1766. Tree of Coprimes
# Hard

# 42

# 4

# Add to List

# Share
# There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a value associated with it, and the root of the tree is node 0.

# To represent this tree, you are given an integer array nums and a 2D array edges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree.

# Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.

# An ancestor of a node i is any other node on the shortest path from node i to the root. A node is not considered an ancestor of itself.

# Return an array ans of size n, where ans[i] is the closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ancestor.

 

# Example 1:



# Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
# Output: [-1,0,0,1]
# Explanation: In the above figure, each node's value is in parentheses.
# - Node 0 has no coprime ancestors.
# - Node 1 has only one ancestor, node 0. Their values are coprime (gcd(2,3) == 1).
# - Node 2 has two ancestors, nodes 1 and 0. Node 1's value is not coprime (gcd(3,3) == 3), but node 0's
#   value is (gcd(2,3) == 1), so node 0 is the closest valid ancestor.
# - Node 3 has two ancestors, nodes 1 and 0. It is coprime with node 1 (gcd(3,2) == 1), so node 1 is its
#   closest valid ancestor.
# Example 2:



# Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
# Output: [-1,0,-1,0,0,0,-1]
 

# Constraints:

# nums.length == n
# 1 <= nums[i] <= 50
# 1 <= n <= 105
# edges.length == n - 1
# edges[j].length == 2
# 0 <= uj, vj < n
# uj != vj

# This solution works:

class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        self.N = len(nums)
        self.nums = nums

        self.is_coprime = [[False for _ in range(51)] for _ in range(51)]
        for n1 in range(1, 51):
            for n2 in range(1, 51):
                coprime = True
                for divisor in range(2, 51):
                    if n1 % divisor == 0 and n2 % divisor == 0:
                        coprime = False
                        break
                self.is_coprime[n1][n2] = coprime
        
        self.adj = {i: set([]) for i in range(self.N)}
        for n1, n2 in edges:
            self.adj[n1].add(n2)
            self.adj[n2].add(n1)
        
        self.ans = [(-1, -1) for _ in range(self.N)]
        self.helper(0, None, {}, 0)
        return [elem[0] for elem in self.ans]
    
    def helper(self, node, prev, seen_nums, depth):
        num = self.nums[node]
        for num2 in range(1, 51):
            if self.is_coprime[num][num2] and num2 in seen_nums:
                coprime_node, coprime_depth = seen_nums[num2]
                if coprime_depth > self.ans[node][1]:
                    self.ans[node] = coprime_node, coprime_depth

        old = None
        if num in seen_nums:
            old = seen_nums[num]
    
        seen_nums[num] = node, depth
        for nxt in self.adj[node]:
            if nxt != prev:
                self.helper(nxt, node, seen_nums, depth + 1)

        if old is not None:
            seen_nums[num] = old
        else:
            del seen_nums[num]
        