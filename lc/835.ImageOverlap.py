# 835. Image Overlap
# Medium

# 446

# 631

# Add to List

# Share
# Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

# We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

# (Note also that a translation does not include any kind of rotation.)

# What is the largest possible overlap?

# Example 1:

# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]
#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
# Output: 3
# Explanation: We slide A to right by 1 unit and down by 1 unit.
# Notes: 

# 1 <= A.length = A[0].length = B.length = B[0].length <= 30
# 0 <= A[i][j], B[i][j] <= 1


# # THESE APPROACHES DO NOT WORK :
# class Solution:
#     def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
#         a = set([])
#         b = set([])
#         m = len(A)
#         n = len(A[0])
        
#         for row in range(m):
#             for col in range(n):
#                 if A[row][col] == 1:
#                     a.add((row,col))
#                 if B[row][col] == 1:
#                     b.add((row,col))
#         max_overlap = 0
#         for num in range(1,m+1):
#             overlap = 0
#             for row, col in ((0,num),(0,-num),(num,0),(-num,0)):
#                 for r, c in a:
#                     if 0<=r+row<=m-1 and 0<=c+col<=n-1 and (r+row, c+col) in b: 
#                         # print((r+row, c+col))
#                         overlap+=1
#                 max_overlap=max(max_overlap,overlap)

#         return max_overlap


# debug effors ---:

# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]

#        B = [[0,0,0],
#             [0,1,1],
#             [0,0,1]]
       
       
       
# B= [[0,0,0],
#     [0,1,1],
#     [0,0,1]]

# (1,1), (1,2)
#        (2,2)
       
# r -1 
# c -1 



# Input: A = [[1,1,0],
#             [0,1,0],
#             [0,1,0]]

#             B = [[0,0,0],
#                 [0,1,1],
#                 [0,0,1]]

# THIS APPROACH DOES NOT WORK:

# class Solution:
#     def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
#         '''
#         min = 0
#         max = min(# of 1 in b, # of 1 in a)
#         '''
#         a = set([])
#         b = set([])
#         m = len(A)
#         n = len(A[0])
        
#         for row in range(m):
#             for col in range(n):
#                 if A[row][col] == 1:
#                     a.add((row,col))
#                 if B[row][col] == 1:
#                     b.add((row,col))
        
#         if len(a)<len(b):
#             a,b=b,a
            
#         def helper(r,c):
#             if not 0<=r<=m-1 or not 0<=c<=n-1:
#                 return 
#             max_overlap = 0
            
#             overlap = 0 
#             if (r, c) in b:
#                 overlap +=1
            
#             for num in range(1,m+1):
#                 overlap = 0
#                 for row, col in ((0,num),(0,-num),(num,0),(-num,0)):
#                     for r, c in b:
#                         max_overlap = max(overlap + max_overlap,overlap + helper(row+r,col+c))
#             return max_overlap
#         return helper()
#         # for num in range(1,m+1):
#         #     overlap = 0
#         #     for row, col in ((0,num),(0,-num),(num,0),(-num,0)):
#         #         for r, c in a:
#         #             if 0<=r+row<=m-1 and 0<=c+col<=n-1 and (r+row, c+col) in a: 
#         #                 # print((r+row, c+col))
#         #                 overlap+=1
#         #         max_overlap=max(max_overlap,overlap)

#         # return max_overlap


# THIS SOLUTION WORKS !!!

# USING COUNTER TO JUST CHECK THE OFFCETS :O

from collections import Counter

class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:

        a = []
        b = []
        m = len(A)
        n = len(A[0])
        
        for row in range(m):
            for col in range(n):
                if A[row][col] == 1:
                    a.append((row,col))
                if B[row][col] == 1:
                    b.append((row,col))
        
        offsets = Counter()
        for a_x, a_y in a:
            for b_x, b_y in b:
                offsets[(a_x-b_x, a_y-b_y)] += 1
        if len(offsets) < 1:
            return 0
        return max(offsets.values())


            