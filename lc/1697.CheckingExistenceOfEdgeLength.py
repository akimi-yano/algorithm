# 1697. Checking Existence of Edge Length Limited Paths
# Hard

# 49

# 3

# Add to List

# Share
# An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

# Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

# Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

# Example 1:


# Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
# Output: [false,true]
# Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
# For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
# For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
# Example 2:


# Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
# Output: [true,false]
# Exaplanation: The above figure shows the given graph.
 

# Constraints:

# 2 <= n <= 105
# 1 <= edgeList.length, queries.length <= 105
# edgeList[i].length == 3
# queries[j].length == 3
# 0 <= ui, vi, pj, qj <= n - 1
# ui != vi
# pj != qj
# 1 <= disi, limitj <= 109
# There may be multiple edges between two nodes.


# This approach does not work 

# class Solution:
#     def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
#         adj_list = {}
#         for n1, n2, d in edgeList:
#             if n1 not in adj_list:
#                 adj_list[n1] = {}
#             if n2 not in adj_list[n1]:
#                 adj_list[n1][n2] = d
#             else:
#                 adj_list[n1][n2] = min(adj_list[n1][n2], d)
            
#             if n2 not in adj_list:
#                 adj_list[n2] = {}
#             if n1 not in adj_list[n2]:
#                 adj_list[n2][n1] = d
#             else:
#                 adj_list[n2][n1] = min(adj_list[n2][n1], d)
#         print(adj_list)
#         # need to remove duplicate key
#         # {0: [(1, 2), (2, 8), (1, 16)], 1: [(0, 2), (2, 4), (0, 16)], 2: [(1, 4), (0, 8)]}
#         # {0: {1:2, 2:8}, 1: {(0, 2), (2, 4), (0, 16)], 2: [(1, 4), (0, 8)]}


# This solution works 

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.roots = [i for i in range(n)]
        ans = [False for _ in range(len(queries))]
        # sort both edgelist and queries 
        edgeList.sort(key = lambda trio : trio[2])
        edge_idx = 0 # index of the edge I am processing 
        queries = [query + [i] for i, query in enumerate(queries)] # process queries to include index as well
        for q_n1, q_n2, limit, idx in sorted(queries, key = lambda quadro : quadro[2]):
            while edge_idx < len(edgeList) and edgeList[edge_idx][2] < limit:
                e_n1, e_n2, _ = edgeList[edge_idx]
                self.union(e_n1, e_n2)
                edge_idx += 1
            ans[idx] = self.find(q_n1) == self.find(q_n2)
        return ans     
        
    def union(self, real_x, real_y):
        x = self.find(real_x)
        y = self.find(real_y)        
        if x < y:
            self.roots[y] = x
        elif x > y:
            self.roots[x] = y

    def find(self, x):
        if x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
        