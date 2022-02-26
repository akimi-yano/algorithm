# 847. Shortest Path Visiting All Nodes
# Hard

# 1338

# 98

# Add to List

# Share
# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

# Example 1:


# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]
# Example 2:


# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]
 

# Constraints:

# n == graph.length
# 1 <= n <= 12
# 0 <= graph[i].length < n
# graph[i] does not contain i.
# If graph[a] contains b, then graph[b] contains a.
# The input graph is always connected.


# This solution works:


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0
        
        n = len(graph)
        ending_mask = (1 << n) - 1
        queue = [(node, 1 << node) for node in range(n)]
        seen = set(queue)

        steps = 0
        while queue:
            next_queue = []
            for i in range(len(queue)):
                node, mask = queue[i]
                for neighbor in graph[node]:
                    next_mask = mask | (1 << neighbor)
                    if next_mask == ending_mask:
                        return 1 + steps
                    
                    if (neighbor, next_mask) not in seen:
                        seen.add((neighbor, next_mask))
                        next_queue.append((neighbor, next_mask))
            
            steps += 1
            queue = next_queue
            
        '''
        Approach 2: Breadth-First Search (BFS)
        
        Intuition

        The previous approach is comparatively slow but works because the bounds are small. The main problem is that we are working backwards and need a DFS starting from every node. The optimal path may end at node 0, but we still need to check all other nodes to make sure. As with any problem that asks us to find the shortest path, it may be more intuitive to approach this problem using BFS.

        Because BFS guarantees the shortest path in an unweighted graph, as soon as we find an answer, we know it is the optimal one, unlike in the previous solution where we needed to explore all reachable states to make sure.

        This approach is similar to the previous one in terms of logic. However, instead of using top-down dynamic programming in the form of DFS + memoization, we will perform BFS by implementing a queue. Instead of starting at endingMask, we will start at the base case masks - only having one bit set to 1, and then work our way towards endingMask.

        Because we were working backwards in the previous approach, for all neighbors, we needed to check (neighbor, mask) and (neighbor, mask ^ (1 << node)). Now, since we're moving forwards, the state we should consider next from each (node, mask) is different. If we are at node A and move to node B, it doesn't matter if we go B -> A -> B or A -> B - in both cases, upon arriving at B, we want our mask to have the bit corresponding to node B set as 1. This is a nice improvement on the previous approach as for each neighbor, we only need to consider 1 possibility instead of 2. Since we always want the bit to be set to 1, we will use an OR operation with 1 << neighbor to make sure the bit is set to 1.

        More formally, for any given state (node, mask), we can traverse to (neighbor, mask | (1 << neighbor)) for all neighbors in graph[node]. We will still need to use some space to ensure that we don't revisit states and create an infinite cycle, but this time we don't need to associate the states with any values, just a flag to indicate if it has been visited yet or not.

        Algorithm

        If graph only contains one node, then return 0 as we can start at node 0 and complete the problem without taking any steps.

        Initialize some variables:

        n, as the length of graph.
        endingMask = (1 << n) - 1, a bitmask that represents all nodes being visited.
        seen, a data structure that will be used to indicate if we have visited a state to prevent cycles.
        queue, a data structure that implements an abstract queue used for our BFS.
        steps, an integer that keeps track of which step we are on. Since BFS gaurantees a shortest path, as soon as we encounter endingMask, we can return steps.
        Populate queue and seen with the base cases (starting at all nodes with the mask set to having only visited the given node). This is (i, 1 << i) for all i from 0 to n - 1.

        Perform a BFS:

        Initialize nextQueue, which will replace queue at the end of the current step.
        Loop through the current queue. For each state (node, mask), loop through graph[node]. For each neighbor, declare a new state (neighbor, nextMask), where nextMask = mask | (1 << neighbor). If nextMask == endingMask, then that means taking one more step to the neighbor will complete visiting all nodes, so return 1 + steps. Otherwise, if this new state has not yet been visited, then add it nextQueue and seen.
        After looping through the current queue, increment steps by 1 and replace queue with nextQueue.
        The constraints state that the input graph is always connected, therefore there will always be an answer. The return statement in the BFS will always trigger, and we don't need to worry about other cases.

        '''