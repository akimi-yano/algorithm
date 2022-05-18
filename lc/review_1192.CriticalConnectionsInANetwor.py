# 1192. Critical Connections in a Network
# Hard

# 3539

# 140

# Add to List

# Share
# There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

# A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

# Return all critical connections in the network in any order.

 

# Example 1:


# Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
# Output: [[1,3]]
# Explanation: [[3,1]] is also accepted.
# Example 2:

# Input: n = 2, connections = [[0,1]]
# Output: [[0,1]]
 

# Constraints:

# 2 <= n <= 105
# n - 1 <= connections.length <= 105
# 0 <= ai, bi <= n - 1
# ai != bi
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