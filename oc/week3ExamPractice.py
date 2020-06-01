# Solved very very quickly !!! So proud !!!

import heapq
def lastStoneWeight(weights):
    maxheap=[]
    for weight in weights:
        heapq.heappush(maxheap,weight*(-1))

    while len(maxheap)>1:
        lar1 = (heapq.heappop(maxheap))*(-1)

        lar2 = (heapq.heappop(maxheap))*(-1)

        if lar1 == lar2:
            pass
        elif lar1> lar2:
            heapq.heappush(maxheap,((lar1-lar2)*(-1)))
        elif lar2> lar1:
            heapq.heappush(maxheap,((lar2-lar1)*(-1)))
    print(maxheap)
    if len(maxheap)==0:
        return 0
    else:
        ans = (heapq.heappop(maxheap))*(-1)
        return ans



def maximumDifference(g_nodes, g_from, g_to):
    adj_list = {}
    for i in range(len(g_from)):
        if g_from[i] not in adj_list:
            adj_list[g_from[i]]=set([g_to[i]])
        else:
            adj_list[g_from[i]].add(g_to[i])
        
        if g_to[i] not in adj_list:
            adj_list[g_to[i]]=set([g_from[i]])
        else:
            adj_list[g_to[i]].add(g_from[i])
    
    def find_smallest(cur_node):
        visited.add(cur_node)
        smallest = cur_node
        for neighbor in adj_list[cur_node]:
            if neighbor not in visited:
                smallest = min(smallest, find_smallest(neighbor))
        return smallest
    
    max_diff = 0
    while len(adj_list) > 0:
        largest = max(adj_list.keys())
        visited = set([])
        smallest = find_smallest(largest)
        max_diff = max(max_diff, largest - smallest)
        for visited_node in visited:
            del adj_list[visited_node]

    return max_diff
print(maximumDifference(5,
                        [-3,-1, 0, 1, 3, 4],
                        [-2, 1, 2, 2, 4, 5]))
# expected to return 3