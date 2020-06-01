
# 1. Maximum Difference
# Given a number of nodes and edges, construct an undirected graph. 
# A connected component of the graph is any group of connected nodes. 
# For each connected component, determine the difference between its maximum and minimum value. 
# Return the maximum of all of these differences.

# For example, given a graph with 4 nodes, connected as follows: {1, 2, 3}, and {4}. 
# The only connected component has a difference 3 - 1 = 2.

# Function Description 

# Complete the function maximumDifference in the editor below. 
# The function must return an integer denoting the maximum difference between the minimum and maximum node values in any connected component.

# maximumDifference has the following parameter(s):
#     g_nodes: the number of nodes
#     g_from[g_from[1],...g_from[g_edges]]:  an array of edge start nodes
#     g_to[g_to[1],...g_to[g_edges]]:  an array of edge end nodes

# Constraints
# 1 ≤ g_nodes ≤ 105
# 1 ≤ g_edges ≤ min(105, (g_nodes × (g_nodes - 1)) / 2)

# Input Format for Custom Testing
# Sample Case 0
# Sample Input 0

# 5 6
# 1 2
# 1 3
# 2 3
# 2 4
# 3 4
# 4 5
# Sample Output 0

# 4
# Explanation 0

# Sample 1
# Graph g.
# The graph has the following connected component:

# A component consisting of nodes {1, 2, 3, 4, 5}. The maximal value node is 5 and the minimal value node is 1, so the difference is 5 − 1 = 4.
# Because there is only one component, we return 4 as our answer.

# Complete the 'maximumDifference' function below.
# The function is expected to return an INTEGER.
# The function accepts UNWEIGHTED_INTEGER_GRAPH g as parameter.

# For the unweighted graph, <name>:
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i].



# this code does not work !!!!
# def maximumDifference(g_nodes, g_from, g_to):
#     adj_list = {}
#     for i in range(len(g_from)):
#         if g_from[i] not in adj_list:
#             adj_list[g_from[i]]=set([g_to[i]])
#         else:
#             adj_list[g_from[i]].add(g_to[i])
        
#         if g_to[i] not in adj_list:
#             adj_list[g_to[i]]=set([g_from[i]])
#         else:
#             adj_list[g_to[i]].add(g_from[i])

#     largest = max(adj_list.keys())
#     prev = largest
#     visited = set([])
#     visited.add(prev)
#     smallest = min(adj_list.keys())
#     max_diff= 0
#     cur = None
#     while cur !=smallest:
        
#         cur = min(adj_list[prev])
#         if cur not in visited:
#             visited.add(cur)
#             prev = cur
#         else:
#             prev=prev-1
#             largest = prev
#         max_diff = max(max_diff,(largest-cur))
#     return max_diff


# WORKING SOLUTION
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


print(maximumDifference(5,[1,1,2,2,3,4],[2,3,3,4,4,5]))
# expected to return 4

print(maximumDifference(5,[1,3,4],[2,4,5]))
# expected to return 2

print(maximumDifference(5,[-3, -1,3,4],[-2, 2,4,5]))
# expected to return 3

print(maximumDifference(5,
                        [-3,-1, 0, 1, 3, 4],
                        [-2, 1, 2, 2, 4, 5]))
# # expected to return 3



# Solved very very quickly !!! So proud !!!
# 2. Crashing stones
# Each day a quarry-worker is given a pile of stones and told to reduce the larger stones into smaller ones. 
# The worker must smash the stones together to reduce them, and is told to always pick up the largest two stones and smashe them together. 
# If the stones are of equal weight, they both disintegrate entirely. 
# If one is larger, the smaller one is disintegrated and the larger one is reduced by the weight of the smaller one. 
# Eventually, there is either one stone left that cannot be broken, or all of the stones have been smashed. 
# Determine the weight of the last stone, or return 0 if there is none.

# Example
# weights = [1,2,3,6,7,7].

# The worker always starts with the two largest stones. 
# In this case, the two largest stones have equal weights of 7 so they both disintegrate when smashed. 
# Next the worker smashes weights 3 and 6. The smaller one is destroyed and the larger weighs 6 - 3 = 3 units. 
# Then, weights 3 and 2 are smashed together, which leaves a stone of weight 1. 
# This is smashed with the last remaining stone of weight 1. 
# There are no stones left, so the remaining stone weight is 0.
# Function Description

# Complete the function lastStoneWeight in the editor below. 
# The function must return an integer that denotes the weight of the last stone, or 0 if all stones shattered into dust.

# lastStoneWeight has the following parameter(s):

#     int weights[n]:  an array of integers indicating the weights of each stone

# Constraints
# 1 ≤ n ≤ 105
# 1 ≤ weights[i] ≤ 109

# Input Format for Custom Testing
# Sample Case 0
# Sample Input

# STDIN    Function
# -----    --------
# 3     →  weights[] size n = 3
# 2     →  weights = [2, 4, 5]
# 4
# 5
# Sample Output

# 1
# Explanation
# First the worker takes stones with weights 4 and 5 and crashes them into each other. 
# The first one disintegrates completely. The second one is reduced to a weight of 1. 
# Next the worker crashes that stone into the last stone with weight 2. 
# The smaller stone disintegrates, and the last stone is reduced to a weight of 1.


# Complete the 'lastStoneWeight' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY weights as parameter.


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
    if len(maxheap)==0:
        return 0
    else:
        ans = (heapq.heappop(maxheap))*(-1)
        return ans
print(lastStoneWeight([1,2,3,6,7,7])) 
# expected to return 0

print(lastStoneWeight([2,4,5]))
# expected to return 1