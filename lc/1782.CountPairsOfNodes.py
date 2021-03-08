# 1782. Count Pairs Of Nodes
# Hard

# 66

# 39

# Add to List

# Share
# You are given an undirected graph represented by an integer n, which is the number of nodes, and edges, where edges[i] = [ui, vi] which indicates that there is an undirected edge between ui and vi. You are also given an integer array queries.

# The answer to the jth query is the number of pairs of nodes (a, b) that satisfy the following conditions:

# a < b
# cnt is strictly greater than queries[j], where cnt is the number of edges incident to a or b.
# Return an array answers such that answers.length == queries.length and answers[j] is the answer of the jth query.

# Note that there can be repeated edges.

 

# Example 1:


# Input: n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
# Output: [6,5]
# Explanation: The number of edges incident to at least one of each pair is shown above.
# Example 2:

# Input: n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
# Output: [10,10,9,8,6]
 

# Constraints:

# 2 <= n <= 2 * 104
# 1 <= edges.length <= 105
# 1 <= ui, vi <= n
# ui != vi
# 1 <= queries.length <= 20
# 0 <= queries[j] < edges.length


# This approach does not work:

# from collections import Counter
# class Solution:
#     def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
#         degree = [0 for _ in range(n+1)]
#         edge_count = Counter()
#         for node1, node2 in edges:
#             degree[node1] += 1
#             degree[node2] += 1
            
#             if node1 > node2:
#                 node1, node2 = node2, node1
#             edge_count[(node1, node2)] += 1
            
#         sorted_degrees = list(sorted(degree[1:]))
#         ans = []    
        
#         for threshold in queries:
#             count = 0
#             # create pairs 
            
#             # reduce counts
            
#             ans.append(count)


# This solution works - handling double counting later to reduce the time complexity:

from collections import Counter
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0 for _ in range(n+1)]
        edge_count = Counter()
        for node1, node2 in edges:
            degree[node1] += 1
            degree[node2] += 1
            
            if node1 > node2:
                node1, node2 = node2, node1
            edge_count[(node1, node2)] += 1
            
        sorted_degrees = list(sorted(degree[1:]))
        ans = []    
        
        for threshold in queries:
            count = 0
            
            # create pairs or on its own
            r = n
            for l in range(n-1):
                while l < r-1 and sorted_degrees[l]+sorted_degrees[r-1] > threshold:
                    r -= 1
                if l < r:
                    # pair of left(small one) and right (big one)
                    count += n - r
                else:
                    # just using left(which can be big enough on its own)
                    count += n - l - 1
            
            # reduce counts  - look for the ones that 2 of them together is larger than threshold but if we subtract edge_count (duplicates/ counting multiple times), then not meeting the threshold -> subtract 1 from count
            for n1, n2, in edge_count:
                if degree[n1] + degree[n2] > threshold and degree[n1] + degree[n2] - edge_count[(n1, n2)] <= threshold:
                    count -= 1
            
            ans.append(count)
            
        return ans