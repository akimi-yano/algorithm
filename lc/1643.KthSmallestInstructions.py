# 1643. Kth Smallest Instructions
# Hard

# 41

# 2

# Add to List

# Share
# Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can only travel right and down. You are going to help Bob by providing instructions for him to reach destination.

# The instructions are represented as a string, where each character is either:

# 'H', meaning move horizontally (go right), or
# 'V', meaning move vertically (go down).
# Multiple instructions will lead Bob to destination. For example, if destination is (2, 3), both "HHHVV" and "HVHVH" are valid instructions.

# However, Bob is very picky. Bob has a lucky number k, and he wants the kth lexicographically smallest instructions that will lead him to destination. k is 1-indexed.

# Given an integer array destination and an integer k, return the kth lexicographically smallest instructions that will take Bob to destination.

 

# Example 1:



# Input: destination = [2,3], k = 1
# Output: "HHHVV"
# Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
# ["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
# Example 2:



# Input: destination = [2,3], k = 2
# Output: "HHVHV"
# Example 3:



# Input: destination = [2,3], k = 3
# Output: "HHVVH"
 

# Constraints:

# destination.length == 2
# 1 <= row, column <= 15
# 1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b​​​​​.

# This approach does not work !

# import heapq
# class Solution:
#     def kthSmallestPath(self, destination: List[int], k: int) -> str:
        
#         self.ROW = destination[0]
#         self.COL = destination[1]
#         self.K = k
#         memo = {}
#         def helper(row, col, path):
#             key = (row, col, path)
#             if key in memo:
#                 return memo[key]
            
#             if row == self.ROW and col == self.COL:
#                 return [[]]
#             if not 0<=row<=self.ROW or not 0<=col<=self.COL:
#                 return []
#             temp = []
#             [temp.append(["H"]+elem) for elem in helper(row+1,col, path)]
#             [temp.append(["V"]+elem) for elem in helper(row,col+1, path)]
#             return temp 
        
#         all_ins = ["".join(elem) for elem in helper(0,0,"")]
       
#         max_heap = []
#         for elem in all_ins:
#             heapq.heappush(max_heap, elem)
#             if len(max_heap)> self.K:
#                 heapq.heappop(max_heap)
#         ans = ""
#         for elem in max_heap[0]:
#             if elem == "V":
#                 ans += "H"
#             else:
#                 ans += "V"
#         return ans
        
        
# This solution works !
'''
very special problem ! when find kth ... problems we do this sometimes (but sometimes its just heap, sort or quick select)
'''
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        self.ROW = destination[0]
        self.COL = destination[1]
        self.memo = {}
        
        self.ans = ''
        self.build_path(k, 0, 0)
        return self.ans
    
    def build_path(self, k, r, c):
        if c < self.COL:
            num = self.num_ways(r, c+1)
            if k <= num:
                self.ans += 'H'
                self.build_path(k, r, c+1)
            else:
                self.ans += 'V'
                self.build_path(k-num, r+1, c)
        elif r < self.ROW:
            self.ans += 'V'
            self.build_path(k, r+1, c)
        else:
            pass
            
    
    def num_ways(self, r, c):
        key = (r, c)
        if key in self.memo:
            return self.memo[key]

        ans = 0
        if r == self.ROW and c == self.COL:
            ans = 1
        if r < self.ROW:
            ans += self.num_ways(r+1, c)
        if c < self.COL:
            ans += self.num_ways(r, c+1)
        self.memo[key] = ans
        return ans