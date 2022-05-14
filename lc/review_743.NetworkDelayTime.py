# 743. Network Delay Time
# Medium

# 4041

# 275

# Add to List

# Share
# You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

# Example 1:


# Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
# Output: 2
# Example 2:

# Input: times = [[1,2,1]], n = 2, k = 1
# Output: 1
# Example 3:

# Input: times = [[1,2,1]], n = 2, k = 2
# Output: -1
 

# Constraints:

# 1 <= k <= n <= 100
# 1 <= times.length <= 6000
# times[i].length == 3
# 1 <= ui, vi <= n
# ui != vi
# 0 <= wi <= 100
# All the pairs (ui, vi) are unique. (i.e., no multiple edges.)


# This solution works:


import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        minheap = []
        cur_dist = 0
        heapq.heappush(minheap,(cur_dist,K))
        
        remaining = set([i for i in range(1,N+1)])
        adj_list = {}
        for start, goal, dist in times:
            if start not in adj_list:
                adj_list[start] = [(dist, goal)]
            else:
                adj_list[start].append((dist, goal))
        
        while len(minheap)>0 and len(remaining)>0:
            dist,node = heapq.heappop(minheap)
            if node not in remaining:
                continue
            remaining.remove(node)
            cur_dist = dist
            if node in adj_list:
                for next_dist, next_node in adj_list[node]:
                    heapq.heappush(minheap,(cur_dist+next_dist,next_node))
        return cur_dist if len(remaining) == 0 else -1