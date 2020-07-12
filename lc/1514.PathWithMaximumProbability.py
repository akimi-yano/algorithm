# 1514. Path with Maximum Probability
# Medium

# 26

# 2

# Add to List

# Share
# You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b] is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return its success probability.

# If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by at most 1e-5.

 

# Example 1:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
# Output: 0.25000
# Explanation: There are two paths from start to end, one having a probability of success = 0.2 and the other has 0.5 * 0.5 = 0.25.
# Example 2:



# Input: n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
# Output: 0.30000
# Example 3:



# Input: n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
# Output: 0.00000
# Explanation: There is no path between 0 and 2.
 

# Constraints:

# 2 <= n <= 10^4
# 0 <= start, end < n
# start != end
# 0 <= a, b < n
# a != b
# 0 <= succProb.length == edges.length <= 2*10^4
# 0 <= succProb[i] <= 1
# There is at most one edge between every two nodes.

import heapq
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # dijkistra with max heap
        # if you see weighted graph and find the most oo or least oo do dijkistra
        adj_list = {}
        for i in range(len(edges)):
            if edges[i][0] not in adj_list:
                adj_list[edges[i][0]] = [(succProb[i],edges[i][1])]
            else:
                adj_list[edges[i][0]].append((succProb[i],edges[i][1]))
            if edges[i][1] not in adj_list:
                adj_list[edges[i][1]] = [(succProb[i],edges[i][0])]
            else:
                adj_list[edges[i][1]].append((succProb[i],edges[i][0]))
        print(adj_list)
        cur_prob = -1
        maxheap = [(cur_prob,start)]
        seen = set([])
        while maxheap:
            # print(maxheap)
            prob, cur_node = heapq.heappop(maxheap)
            prob*=(-1)
            # print(prob)
            if cur_node == end:
                return prob
            if cur_node in seen:
                continue
            seen.add(cur_node)
            cur_prob = prob
            if cur_node in adj_list:
                for next_prob, next_node in adj_list[cur_node]:
                    if next_node not in seen:
                        heapq.heappush(maxheap,((cur_prob*next_prob)*(-1),next_node))
        return 0
                    
