# 1615. Maximal Network Rank
# Medium

# 20

# 1

# Add to List

# Share
# There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi] indicates that there is a bidirectional road between cities ai and bi.

# The network rank of two different cities is defined as the total number of directly connected roads to either city. If a road is directly connected to both cities, it is only counted once.

# The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

# Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

 

# Example 1:



# Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
# Output: 4
# Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1. The road between 0 and 1 is only counted once.
# Example 2:



# Input: n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
# Output: 5
# Explanation: There are 5 roads that are connected to cities 1 or 2.
# Example 3:

# Input: n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
# Output: 5
# Explanation: The network rank of 2 and 5 is 5. Notice that all the cities do not have to be connected.
 

# Constraints:

# 2 <= n <= 100
# 0 <= roads.length <= n * (n - 1) / 2
# roads[i].length == 2
# 0 <= ai, bi <= n-1
# ai != bi
# Each pair of cities has at most one road connecting them.

# This solution works :
    
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj_list = {}
        for n1, n2 in roads:

            if n1 not in adj_list:
                adj_list[n1] = set([])
            adj_list[n1].add(n2)
            
            if n2 not in adj_list:
                adj_list[n2] = set([])
            adj_list[n2].add(n1)
        
        max_num = 0
        for n1, connects1 in adj_list.items():
            for n2, connects2 in adj_list.items():
                if n1 == n2:
                    continue
                n1_counts = len(connects1)
                n2_counts = len(connects2)
                if n1 in connects2:
                    max_num = max(max_num, n1_counts + n2_counts -1)
                else:
                    max_num = max(max_num, n1_counts + n2_counts)
        return max_num
            