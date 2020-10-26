# 1632. Rank Transform of a Matrix
# Hard

# 86

# 6

# Add to List

# Share
# Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

# The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

# If an element is the smallest element in its row and column, then its rank is 1.
# If two elements p and q are in the same row or column, then:
# If p < q then rank(p) < rank(q)
# If p == q then rank(p) == rank(q)
# If p > q then rank(p) > rank(q)
# The rank should be as small as possible.
# It is guaranteed that answer is unique under the given rules.

 

# Example 1:


# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row and column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1], matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank 2.
# Example 2:


# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
# Example 3:


# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
# Example 4:


# Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
# Output: [[5,1,4],[1,2,3],[6,3,1]]


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# -109 <= matrix[row][col] <= 109

# This solution works !:

'''
union find with rank
update the root to be larger rank node
each row and col are represented as nodes by doing [ row1, row2, row3, maxrow+col1, maxrow+col2, maxrow+col3 ]
update the rank to be max+1 each time
'''

class Solution:
    def union(self, a, b):
        aroot, broot = self.find(a), self.find(b)
        # set the root to be the one with the bigger rank
        if self.ranks[aroot] > self.ranks[broot]:
            self.roots[broot] = aroot
        else:
            self.roots[aroot] = broot
        
    def find(self, a):
        if a != self.roots[a]:
            self.roots[a] = self.find(self.roots[a])
        return self.roots[a]
    
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        R = len(matrix)
        C = len(matrix[0])
        d = {}
        rowranks = [0 for _ in range(R)]
        colranks = [0 for _ in range(C)]
        ans = [[0 for _ in range(C)] for _ in range(R)]
        
        # first, group all the locations with the same number in a dictionary
        for r in range(R):
            for c in range(C):
                num = matrix[r][c]
                if num not in d:
                    d[num] = []
                d[num].append((r, c))
        
        # iterate through the number-locations pairs in ascending order
        for num in sorted(d):
            # prepare the roots and ranks for doing Union Find
            # the first R numbers represent the rows, the next C numbers represent the columns
            self.roots = [i for i in range(R)] + [R + i for i in range(C)]
            self.ranks = rowranks + colranks
    
            locations = d[num]
            for r, c in locations:
                r_node, c_node = r, R + c
                # Union the row and column
                self.union(r_node, c_node)
            
            for r, c in locations:
                # get the root and the rank for this row/column, and update the answer matrix, row ranks and column ranks
                root = self.find(r) # == self.find(R+c)
                rank = self.ranks[root] + 1
                ans[r][c] = rank
                rowranks[r] = rank
                colranks[c] = rank

        return ans