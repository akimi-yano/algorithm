# 1192. Critical Connections in a Network
# Hard

# 2345

# 119

# Add to List

# Share
# There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some server unable to reach some other server.

# Return all critical connections in the network in any order.

 

# Example 1:



# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
 

# Constraints:

# 1 <= n <= 10^5
# n-1 <= connections.length <= 10^5
# connections[i][0] != connections[i][1]
# There are no repeated connections.


# This solution works:

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        '''
        Tarjan's algorithm: if its part of a cycle, it is not critical connection
        so remove it from the answer options
        '''
        
        def dfs(node, parent, prevLabel):
            if labels[node] >= 0:
                return labels[node]
            # assign labels for current node
            labels[node] = prevLabel + 1
            
            minLabel = float('inf')
            
            for nextnode in graph[node]:
                if nextnode == parent:
                    continue
                    
                recursiveLabel = dfs(nextnode, node, labels[node])

                # if nextnode and current node are both part of cycle
                if labels[node] >= recursiveLabel:
                    ans.remove((min(nextnode,node), max(nextnode,node)))

                minLabel = min(minLabel, recursiveLabel)
            return minLabel
        
        graph = defaultdict(list)
        ans = set()
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
            ans.add((min(u,v), max(u,v)))
            
        labels = [-1] * n
        dfs(0,-1,0)
        return ans