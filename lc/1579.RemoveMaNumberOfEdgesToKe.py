# 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
# Hard

# 33

# 0

# Add to List

# Share
# Alice and Bob have an undirected graph of n nodes and 3 types of edges:

# Type 1: Can be traversed by Alice only.
# Type 2: Can be traversed by Bob only.
# Type 3: Can by traversed by both Alice and Bob.
# Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

# Return the maximum number of edges you can remove, or return -1 if it's impossible for the graph to be fully traversed by Alice and Bob.

 

# Example 1:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
# Output: 2
# Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
# Example 2:



# Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
# Output: 0
# Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
# Example 3:



# Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
# Output: -1
# Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

# Constraints:

# 1 <= n <= 10^5
# 1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
# edges[i].length == 3
# 1 <= edges[i][0] <= 3
# 1 <= edges[i][1] < edges[i][2] <= n
# All tuples (typei, ui, vi) are distinct.



# THIS SOLUTION DOES NOT WORK BECAUSE IT DOES NOT DETECT CYCLE 1

# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         '''
#         all of them are connected so the only possibility that is invalid is that its only type 1 or only type2 -> -1
#         the rest is 0 - 
#         find cycles ?
#         find if we have type3, we dont need type1 or type2 -> check if we have enough type 3 (if not put in the arr)
#         then we check type 1 and 2 
#         also type 3 
#         '''
#         # edges = sorted(edges,key= lambda elem: elem[2])
#         remove = 0
#         found_nodes = {}
#         for ty,fr,to in edges:
#             if ty == 3:
#                 # if fr not in found_nodes or to not in found_nodes:
#                 if fr not in found_nodes:
#                     found_nodes[fr]=0
#                 if to not in found_nodes:
#                     found_nodes[to]=0
#                 found_nodes[fr]+=1
#                 found_nodes[to]+=1
#                     # found_nodes.add(fr)
#                     # found_nodes.add(to)
#                 # else:
#                     # I need to wisely choose which one to remove instead of letting loop decide 
#                     # remove +=1
#         # print(found_nodes)
        
#         print(found_nodes)
#         missing_nodes1 = set([])
#         missing_nodes2 = set([])
#         for node in range(1,n+1):
#             if node not in found_nodes:
#                 missing_nodes1.add(node)
#                 missing_nodes2.add(node)
#         # print(missing_nodes1,missing_nodes2)
        
#         for ty,fr,to in edges:
#             if ty == 1:
#                 if fr not in missing_nodes1 and to not in missing_nodes1:
#                     remove+=1
#                 else:
#                     if fr in missing_nodes1:
#                         missing_nodes1.remove(fr)
#                     if to in missing_nodes1:
#                         missing_nodes1.remove(to)
               
#             elif ty ==2:
#                 if fr not in missing_nodes2 and to not in missing_nodes2:
#                     remove+=1
#                 else:
#                     if fr in missing_nodes2:
#                         missing_nodes2.remove(fr)
#                     if to in missing_nodes2:
#                         missing_nodes2.remove(to)
               
#         # print(missing_nodes1,missing_nodes2)
#         return remove if (not missing_nodes1 and not missing_nodes2) else -1
            



# THIS SOLUTION DOES NOT WORK BECAUSE IT DOES NOT DETECT CYCLE 2

# class Solution:
#     def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
#         '''
#         all of them are connected so the only possibility that is invalid is that its only type 1 or only type2 -> -1
#         the rest is 0 - 
#         find cycles ?
#         find if we have type3, we dont need type1 or type2 -> check if we have enough type 3 (if not put in the arr)
#         then we check type 1 and 2 
#         also type 3 
#         '''
#         edges = sorted(edges,key= lambda elem: elem[1])
#         remove = 0
#         found_nodes = set([])
#         for ty,fr,to in edges:
#             if ty == 3:
#                 if fr not in found_nodes or to not in found_nodes:
#                     found_nodes.add(fr)
#                     found_nodes.add(to)
#                 else:
#                     remove +=1
#         # print(found_nodes)
#         missing_nodes1 = set([])
#         missing_nodes2 = set([])
#         for node in range(1,n+1):
#             if node not in found_nodes:
#                 missing_nodes1.add(node)
#                 missing_nodes2.add(node)
#         # print(missing_nodes1,missing_nodes2)
        
#         for ty,fr,to in edges:
#             if ty == 1:
#                 if fr not in missing_nodes1 and to not in missing_nodes1:
#                     remove+=1
#                 else:
#                     if fr in missing_nodes1:
#                         missing_nodes1.remove(fr)
#                     if to in missing_nodes1:
#                         missing_nodes1.remove(to)
               
#             elif ty ==2:
#                 if fr not in missing_nodes2 and to not in missing_nodes2:
#                     remove+=1
#                 else:
#                     if fr in missing_nodes2:
#                         missing_nodes2.remove(fr)
#                     if to in missing_nodes2:
#                         missing_nodes2.remove(to)
               
#         # print(missing_nodes1,missing_nodes2)
#         return remove if (not missing_nodes1 and not missing_nodes2) else -1

# MY DEBUG EFFORTS: 
# N=13
# arr=[[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]]


# one = []
# two = []
# three = []
# for elem in arr:
#     if elem[0]==1:
#         one.append(elem)
#     elif elem[0]==2:
#         two.append(elem)
#     else:
#         three.append(elem)
# # print(three)
# for elem in three:
#     print("THREE:", elem)
    
# print("*"*50)
# # print(two)
# for elem in one:
#     print("ONE:", elem)
    
# print("*"*50)
# # print(one)
# for elem in two:
#     print("TWO:", elem)



# THIS SOLUTION WORKS !!!!!!!!!!!!!!!!

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        all of them are connected so the only possibility that is invalid is that its only type 1 or only type2 -> -1
        the rest is 0 - 
        find cycles ?
        find if we have type3, we dont need type1 or type2 -> check if we have enough type 3 
        then we check type 1 and 2 
        UNION FIND !!!
        '''
        root = [k for k in range(n+1)]
       
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        
        def union(val1,val2):
            val1,val2 = find(val1),find(val2)
            if val1 == val2:
                return 1
            root[val1] = val2
            return 0
        
        remove = t1 = t2 = 0
        for ty,fr,to in edges:
            if ty == 3:
                if union(fr,to):
                    remove += 1
                else:
                    t1 +=1
                    t2 +=1

        temp_root = root[:]
        for ty,fr,to in edges:
            if ty == 1:
                if union(fr,to):
                    remove += 1
                else:
                    t1 += 1
                        
        root = temp_root
        for ty,fr,to in edges:       
            if ty == 2:
                if union(fr,to):
                    remove += 1
                else:
                    t2 += 1
               
        return remove if (t1 == t2 == n-1) else -1
            