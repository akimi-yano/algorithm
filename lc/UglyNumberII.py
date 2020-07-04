#   Ugly Number II
# Write a program to find the n-th ugly number.

# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# Example:

# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
# Note:  

# 1 is typically treated as an ugly number.
# n does not exceed 1690.

# this TLE
# class Solution:
#     def nthUglyNumber(self, n: int) -> int:
#         memo = {}

#         def is_ugly(num):
#             while num >0:
#                 while num%2==0:   
#                     num = num//2
#                     if num in memo:
#                         return memo[num]
#                 if num ==1:
#                     return True
#                 else: 
#                     while num%3==0:   
#                         num = num//3
#                         if num in memo:
#                             return memo[num]
#                     if num ==1:
#                         return True
#                     else: 
#                         while num%5==0:   
#                             num = num//5
#                             if num in memo:
#                                 return memo[num]
#                         if num ==1:
#                             return True
#                         else:
#                             return False
        
#         count = 1
#         i = 2
#         while count < n:
#             print(count,n,i)
#             ugly = is_ugly(i)
#             if ugly:
#                 count+=1
#             memo[i]=ugly
#             i+=1
#         return i-1
        
        # Ugly numbers are positive numbers whose prime factors only include 2, 3, 5
        # from i=1, found a ugly num ->count+=1. if. n==count return i  




# this works

class Solution:
    nodes = {1: [5, 3, 2]}
    uglies = [1]

    def nthUglyNumber(self, n: int) -> int:
        if n < 1:
            return 0

        while n > len(Solution.uglies):
            best_kv = (-1, float('inf'))
            deleted_nodes = []
            for node, nexts in Solution.nodes.items():
                while len(nexts) > 0 and nexts[-1] in Solution.nodes:
                    nexts.pop()
                if len(nexts) < 1:
                    deleted_nodes.append(node)
                else:
                    if nexts[-1] < best_kv[1]:
                        best_kv = node, nexts[-1]

            Solution.uglies.append(best_kv[1])
            Solution.nodes[best_kv[0]].pop()
            if len(Solution.nodes[best_kv[0]]) < 1:
                del Solution.nodes[best_kv[0]]
            for deleted_node in deleted_nodes:
                del Solution.nodes[deleted_node]
            Solution.nodes[best_kv[1]] = [best_kv[1]*5, best_kv[1]*3, best_kv[1]*2]

        return Solution.uglies[n-1]
        # ans = Solution.uglies[n-1]
        # Solution.nodes = {1: [5, 3, 2]}
        # Solution.uglies = [1]
        # return ans
        

# this works!!!

import heapq

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        visited = set([])
        minheap = [1]

        while n>1:
            while minheap[0] in visited:
                heapq.heappop(minheap)
            ugly = heapq.heappop(minheap)
            visited.add(ugly)
            heapq.heappush(minheap,ugly*2)
            heapq.heappush(minheap,ugly*3)
            heapq.heappush(minheap,ugly*5)
            n-=1
            
        while minheap[0] in visited:
            heapq.heappop(minheap)
        return minheap[0]