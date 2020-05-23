import heapq
import math

def dijkstra(s, e, edges):
    costs = {}
    for node in edges.keys():
        if node == s:
            costs[s] = 0
        else:
            costs[node] = math.inf


    minheap = []
    heapq.heappush(minheap,(costs[s],s))
    known = set([])
    while len(minheap)>0:
        popped = heapq.heappop(minheap)
        cur_cost, cur_node = popped
        # we might have duplicates
        if cur_node in known:
            continue

        known.add(cur_node)
        for edge in edges[cur_node]:
            next_node, edge_cost = edge
            if next_node in known:
                continue
            potential_cost = cur_cost+edge_cost
            if potential_cost >= costs[next_node]:
                continue
            costs[next_node] = potential_cost
            heapq.heappush(minheap,(potential_cost, next_node))
    print(costs)
    return costs[e]
    
    
    # The steps
    # 1 go check all the edges from start - from 1 to 234
    # 2 check if the edges are already visited
    # 3 if not visited yet, check the paths weight by adding my own (weight as of start(0)) + weights that will cost to go through the path to the vertex
    # 4 compare all the potential cost and if they are lowerer, update the cost to lowerer one 
    # 5 choose the lowest path to go 
    # 6 turn the visited to True
    
    
    
    
     # vertex,known,cost,path,trajectory
    

s = '1'
e = '9'
edges = {
    '1': [('2', 2), ('3', 5), ('4', 2)],
    '2': [('1', 2), ('3', 3), ('5', 1)],
    '3': [('1', 5), ('2', 3), ('4', 3), ('5', 1), ('6', 1), ('8', 1)],
    '4': [('1', 2), ('3', 3), ('7', 2)],
    '5': [('2', 1), ('3', 1), ('9', 7)],
    '6': [('3', 1), ('7', 2), ('8', 3)],
    '7': [('4', 2), ('6', 2)],
    '8': [('3', 1), ('6', 3), ('9', 1)],
    '9': [('5', 7), ('8', 1)],
}

print(dijkstra(s, e, edges))