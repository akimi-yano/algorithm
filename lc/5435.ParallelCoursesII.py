# 5435. Parallel Courses II

# This one doesnt work -> look below for a solution that works
# class Solution:
#     def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
#         if len(dependencies)==0:
#             return round(n/k)
#         adj_list = {}
#         reverse_adj = {}
#         all_nodes = set([])
#         for elem in dependencies:
#             if elem[0] not in adj_list:
#                 adj_list[elem[0]]=set([elem[1]])
#             else:
#                 adj_list[elem[0]].add(elem[1])
#             if elem[1] not in reverse_adj:
#                 reverse_adj[elem[1]]=set([elem[0]])
#             else:
#                 reverse_adj[elem[1]].add(elem[0])
            
#             all_nodes.add(elem[0])
#             all_nodes.add(elem[1])
            
#         roots = []    
#         for node in all_nodes:
#             if node not in reverse_adj:
#                 roots.append(node)
#         # print(roots)
#         self.counter = 0
#         self.semester = 0
        
#         def helper(current):
#             if current is None:
#                 return 
#             if current in adj_list:
#                 for next_node in adj_list[current]:
#                     helper(next_node)
            
#             self.counter+=1
#             if self.counter == k:
#                 self.counter = 0
#                 self.semester+=1
        
#         for root in roots:
#             helper(root)
#         rest = n - len(all_nodes)
#         for j in range(rest+1):
#             self.counter+=1
#             if self.counter == k:
#                 self.counter = 0
#                 self.semester+=1
#         return self.semester
        



# This works!
class Solution:
    def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    
        adj_list = {}
        reverse_adj = {}
        all_nodes = set([c for c in range(1, n+1)])
        for elem in dependencies:
            if elem[0] not in adj_list:
                adj_list[elem[0]]=set([elem[1]])
            else:
                adj_list[elem[0]].add(elem[1])
            if elem[1] not in reverse_adj:
                reverse_adj[elem[1]]=set([elem[0]])
            else:
                reverse_adj[elem[1]].add(elem[0])

        def helper(current):
            deepest = 0
            if current in adj_list:
                for next_node in adj_list[current]:
                    depth = 1 + helper(next_node)
                    deepest = max(deepest, depth)
            return deepest

        semester = 0
        while len(all_nodes) > 0:
            can_take = []
            for node in all_nodes:
                if node not in reverse_adj:
                    can_take.append((helper(node), node))
            can_take.sort()
            can_take.reverse()
            for elem in can_take[:k]:
                to_take = elem[1]
                all_nodes.remove(to_take)
                if to_take in adj_list:
                    for blocked in adj_list[to_take]:
                        reverse_adj[blocked].remove(to_take)
                        if len(reverse_adj[blocked]) < 1:
                            del reverse_adj[blocked]
            semester += 1
        return semester
          
        
        