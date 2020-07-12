# 743. Network Delay Time
# There are N network nodes, labelled 1 to N.

# Given times, a list of travel times as directed edges times[i] = (u, v, w), 
# where u is the source node, v is the target node, and w is the time it takes 
# for a signal to travel from source to target.

# Now, we send a signal from a certain node K. How long will it take for all nodes 
# to receive the signal? If it is impossible, return -1.


    # The steps
    # 1 go check all the edges from start - from 1 to 234
    # 2 check if the edges are already visited
    # 3 if not visited yet, check the paths weight by adding my own (weight as of start(0)) + weights that will cost to go through the path to the vertex
    # 4 compare all the potential cost and if they are lowerer, update the cost to lowerer one 
    # 5 choose the lowest path to go 
    # 6 turn the visited to True


import heapq
import math
# this approach tries djikstras algo but not working
# def networkDelayTime(times, N, s):
#     adj_list = {}
#     for time in times:
#         if time[0] not in adj_list:
#             adj_list[time[0]]=[(time[1],time[2])]
#         else:
#             adj_list[time[0]].append((time[1],time[2]))
#     print(adj_list)
#     costs = {}
#     for node in adj_list.keys():
#         if node == s:
#             costs[s] = 0
#         else:
#             costs[node] = math.inf
#     print(costs)
#     minheap = []
#     heapq.heappush(minheap,(costs[s],s))
#     known = set([])
#     print(minheap)
#     while len(minheap)>0:
#         popped = heapq.heappop(minheap)
#         cur_cost, cur_node = popped
#         # we might have duplicates
#         if cur_node in known:
#             continue

#         known.add(cur_node)
#         for edge in adj_list[cur_node]:
#             next_node, edge_cost = edge
#             if next_node in known:
#                 continue
#             potential_cost = cur_cost+edge_cost
#             if next_node  not in costs:
#                 continue
#             if potential_cost >= costs[next_node]:
#                 continue
#             costs[next_node] = potential_cost
#             heapq.heappush(minheap,(potential_cost, next_node))
#     print(costs)
#     print(known)
    
#     if len(known)== N:
#         return max(costs.values())
#     else:
#         return -1
 
# print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)) #output should be 2


# this doest work cuz it doible counts the ones that happen at the same time
#   def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         adj_list = {}
#         for time in times:
#             if time[0] not in adj_list:
#                 adj_list[time[0]]=[(time[1],time[2])]
#             else:
#                 adj_list[time[0]].append((time[1],time[2]))
#         seen = set([])
#         def helper(cur):
#             if cur in seen:
#                 return 0
#             seen.add(cur)
#             if cur not in adj_list:
#                 return 0
#             max_time = 0
#             for next_node in adj_list[cur]:
#                 next_val,time_next =next_node
#                 if next_val not in seen:
#                     max_time=max(max_time,time_next+helper(next_val))
#             return max_time 
#         ans = helper(K) 
#         # print(seen)
#         return ans if len(seen)==N else -1




# Dijkstra's algorithm heap implementation
# first, we build an adjacent list. [0]
# if you don't know what is adjacent list, see https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs

# we use a hash-map 'dis' to keep track of every node's distance to K. [1]
# and we use a priority queue 'pq' to store all the node we encounter and its distance to K. [2]
# which we use a tuple (distance to K, node)

# for every node we visit, if its distance to K is determined, we don't need to look at it anymore. [3]
# because we always pop the nearest one to the K in the priority queue, we can be sure that the distance in 'dis' is the shortest.
# then from the node, which we know the shortest path from K to the node, we keep on explore its neighbors. [4]

# then if we didn't visit every node we return -1, else we return the node which it takes the longest time to reach. [5]

# for time complexity
# we use O(E) to make an adjacency list from edge list.
# we will go through the while loop V-1 times because we need to determined the distance of V-1 other nodes.
# for every loop
# we pop from priority queue (here need O(logE) to get the nearest node).
# we push the node's neighbor to the priority queue d times (which is the degree of the node)
# push the node takes O(logE), we assume all the node is in the queue.
# so every loop we use O(dlogE+logE)~=O(dlogE)
# so total for total, it is O((V-1)(dlogE))+O(E), we know that V-1~=V and V*d=E
# so it is O(ElogE)+O(E)~=O(ElogE)
# E is the number of edges, which is the length of 'times' of the input
# V is the number of node, which is the 'N' of the inout

# for space complexity
# we used O(V) and O(E) in 'dis' and 'pq', and O(E) on the adjacency list.
# so, it is O(V+E).

class Solution(object):
    def networkDelayTime(self, times, N, K):
        aj_list = collections.defaultdict(list) #[0]
        for u, v, w in times: 
            aj_list[u].append((w, v))
        
        dis = {} #[1]
        pq = [(0, K)] #[2]
        
        while pq:
            if len(dis)==N: break
            d, node = heapq.heappop(pq)
            dis[node] = d
            
            for d2, nb in aj_list[node]: #[4]
                if nb not in dis: #[3]
                    heapq.heappush(pq, (d+d2, nb)) #[2]
                    
        return max(dis.values()) if len(dis)==N else -1 #[5]


# DFS solution that does not work !

# class Solution:
#     def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
#         adj_list = {}
#         for time in times:
#             if time[0] not in adj_list:
#                 adj_list[time[0]]=[(time[1],time[2])]
#             else:
#                 adj_list[time[0]].append((time[1],time[2]))
#         seen = set([])
#         def helper(cur):
#             if cur in seen:
#                 return 0
#             seen.add(cur)
#             if cur not in adj_list:
#                 return 0
#             max_time = 0
#             for next_node in adj_list[cur]:
#                 next_val,time_next =next_node
#                 if next_val not in seen:
#                     max_time=max(max_time,time_next+helper(next_val))
#             return max_time 
#         ans = helper(K) 
#         # print(seen)
#         return ans if len(seen)==N else -1



# finally ! solution that works and I am happy with :
    
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