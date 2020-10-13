'''
Question 1: 
1557. Minimum Number of Vertices to Reach All Nodes
link: https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
'''
    # Time O(V+e), Space O(V), runtime =
def findSmallestSetOfVertices(n, edges):
    
    if not edges: return None
    
    seen = set()
    for u,v in edges:
        seen.add(v)
    
    all_nodes = set([x for x in range(n)])
    return all_nodes ^ seen



    # Time O(V+E), Space O(V), runtime = 1176 ms, 94.67%
def findSmallestSetOfVertices(n, edges):
    
    if not edges: return None
    
    g_dict = {key:[] for key in range(n)}
    for u,v in edges:
        g_dict[v].append(u)
    
    result = []
    for k,v in g_dict.items():
        if not v:
            result.append(k)
    return result



'''
Question 2:
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
link: ://leetcode.httpscom/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/
'''

def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
    
    if not edges: return None
    
    dis= [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dis[i][i] = 0
    
    for u,v,w in edges:
        dis[u][v] = w
        dis[v][u] = w
    
    for k in range(n):
        for i in range(n):
            for j in range(i+1,n):
                if dis[i][k] < distanceThreshold and dis[k][j] < distanceThreshold:
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                    dis[j][i] = dis[i][j]
                    
    min_count = float('inf')
    max_city = float('-inf')
    for i in range(n):
        count = 0
        for j in range(n):
            if 0 < dis[i][j] <= distanceThreshold:
                count += 1
        if count <= min_count:
            if (i==3): print(count)
            min_count = count
            max_city = max(i, max_city)
    
    return max_city

'''
DAG -> directed, no cycle
    -> sequence, use topological sort
    
* topological sort.  ---> order of the graph node
    
shortest path:
1. Dijkstra, source, destination, using heap/priority queue, postive weights
2. Bellman-ford  negative weights, similar to Dijstra, 
3. Floyd-warshall, negative weights, Time (v^3), using matrix


1,23,46

Todo = [start node

result_order = []

'''
