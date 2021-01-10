# 1722. Minimize Hamming Distance After Swap Operations
# Medium

# 66

# 2

# Add to List

# Share
# You are given two integer arrays, source and target, both of length n. You are also given an array allowedSwaps where each allowedSwaps[i] = [ai, bi] indicates that you are allowed to swap the elements at index ai and index bi (0-indexed) of array source. Note that you can swap elements at a specific pair of indices multiple times and in any order.

# The Hamming distance of two arrays of the same length, source and target, is the number of positions where the elements are different. Formally, it is the number of indices i for 0 <= i <= n-1 where source[i] != target[i] (0-indexed).

# Return the minimum Hamming distance of source and target after performing any amount of swap operations on array source.

 

# Example 1:

# Input: source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
# Output: 1
# Explanation: source can be transformed the following way:
# - Swap indices 0 and 1: source = [2,1,3,4]
# - Swap indices 2 and 3: source = [2,1,4,3]
# The Hamming distance of source and target is 1 as they differ in 1 position: index 3.
# Example 2:

# Input: source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
# Output: 2
# Explanation: There are no allowed swaps.
# The Hamming distance of source and target is 2 as they differ in 2 positions: index 1 and index 2.
# Example 3:

# Input: source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
# Output: 0
 

# Constraints:

# n == source.length == target.length
# 1 <= n <= 105
# 1 <= source[i], target[i] <= 105
# 0 <= allowedSwaps.length <= 105
# allowedSwaps[i].length == 2
# 0 <= ai, bi <= n - 1
# ai != bi

# This solution works ! - union find !
class Solution:
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if x < y:
                self.roots[y] = x
            else:
                self.roots[x] = y
    def find(self, x):
        if x == self.roots[x]:
            return x
        self.roots[x] = self.find(self.roots[x])
        return self.roots[x]
    
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        target_idx = {}
        for i, val in enumerate(target):
            if val not in target_idx:
                target_idx[val] = set([])
            target_idx[val].add(i)
        # print(target_idx)
        
        self.roots = [i for i in range(len(source))]
        for from_node, to_node in allowedSwaps:
            self.union(from_node, to_node)
        # print(self.roots)
        for i in range(len(self.roots)):
            self.find(i)
        # print(self.roots)
        
        i = 0
        while i < len(source):
            if source[i] != target[i]:
                if source[i] in target_idx:
                    found_idx = None
                    for idx in target_idx[source[i]]:
                    # print(f"checking idx {i} and {idx}")
                        if self.roots[i] == self.roots[idx]:
                            # print(f"swapping {source[i]} and {source[idx]}")
                            source[i], source[idx] = source[idx], source[i]
                            found_idx = idx
                            break
                    if found_idx is not None:
                        target_idx[source[idx]].remove(found_idx)
                        i -= 1
            i += 1
        ans = 0
        # print(source)
        # print(target)
        for i in range(len(source)):
            if source[i] != target[i]:
                ans += 1
        return ans
    
    
# This approach does not work 
# bug because 
# - we must use set([]) as the value of the target index dictionary for duplicate cases
# - after swapping we need to do i -= 1 to go back to make sure the index we just swapped is a value move
# code above is a solution that works!

# class Solution:
#     def union(self, x, y):
#         x = self.find(x)
#         y = self.find(y)
#         if x != y:
#             if x < y:
#                 self.roots[y] = x
#             else:
#                  self.roots[x] = y
#     def find(self, x):
#         if x == self.roots[x]:
#             return x
#         self.roots[x] = self.find(self.roots[x])
#         return self.roots[x]
    
#     def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
#         target_idx = {val: i for i, val in enumerate(target)}
        
#         self.roots = [i for i in range(len(source))]
#         for from_node, to_node in allowedSwaps:
#             self.union(from_node, to_node)
#         # print(self.roots)
#         for i in range(len(self.roots)):
#             self.find(i)
#         # print(self.roots)
#         for i in range(len(source)):
#             if source[i] != target[i]:
#                 if source[i] in target_idx:
#                     idx = target_idx[source[i]]
#                     # print(f"checking idx {i} and {idx}")
#                     if self.roots[i] == self.roots[idx]:
#                         # print(f"swapping {source[i]} and {source[idx]}")
#                         source[i], source[idx] = source[idx], source[i]
#         for i in range(len(source)):
#             if source[i] != target[i]:
#                 if source[i] in target_idx:
#                     idx = target_idx[source[i]]
#                     # print(f"checking idx {i} and {idx}")
#                     if self.roots[i] == self.roots[idx]:
#                         # print(f"swapping {source[i]} and {source[idx]}")
#                         source[i], source[idx] = source[idx], source[i]
#         ans = 0
#         for i in range(len(source)):
#             if source[i] != target[i]:
#                 ans += 1
#         return ans