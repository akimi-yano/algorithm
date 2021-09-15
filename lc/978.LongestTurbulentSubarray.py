# 978. Longest Turbulent Subarray
# Medium

# 964

# 154

# Add to List

# Share
# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
 

# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:

# Input: arr = [100]
# Output: 1
 

# Constraints:

# 1 <= arr.length <= 4 * 104
# 0 <= arr[i] <= 109


# This solution works:


'''
Here we need shortest distances, so Dijkstra algorithm is good idea. First of all, let us forgot about split points, and deal with graph as weighted graph, where weight of each node is number of split points on it plus one. On this graph we perform Dijkstra algorithm. Now at each point we have distance for it from origin. We can find total number of reachable points as:

All original nodes with distance less or equal to M.
For every edge we need to check what we have as distances for it ends:
if both of distances more than M, than we can not reach any split points on this node. If both of them less or equal to M, we can reach some point starting with one end and some points, starting with another end, these two sets can intersect, so we need to remove then number of points in intersection. Also if for one end distance is more than M and for another is less or equal than M, we have only one set of points that can be reached.
Complexity
Time complexity is O(E log N), space complexity is O(N) as for classical Dijkstra algorithm.

'''
class Solution:
    def reachableNodes(self, edges, M, N):
        G = defaultdict(set)
        dist = [float('inf')] * N
        dist[0] = 0
        
        for i, j, w in edges:
            G[i].add((j, w + 1))
            G[j].add((i, w + 1))
            
        heap = [(0, 0)]

        while heap:
            min_dist, idx = heappop(heap)
            for neibh, weight in G[idx]:
                cand = min_dist + weight
                if cand < dist[neibh]:
                    dist[neibh] = cand
                    heappush(heap, (cand, neibh)) 
                    
        ans = sum(dist[i] <= M for i in range(N))
 
        for i, j, w in edges:
            w1, w2 = M - dist[i], M - dist[j]
            ans += (max(0, w1) + max(0, w2))
            if w1 >= 0 and w2 >= 0: ans -= max(w1 + w2 - w, 0)
                
        return ans
