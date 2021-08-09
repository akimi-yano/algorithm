# 1632. Rank Transform of a Matrix
# Hard

# 387

# 24

# Add to List

# Share
# Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

# The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

# The rank is an integer starting from 1.
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

# This solution works: - union find

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        elems = {}
        R, C = len(matrix), len(matrix[0])
        for r in range(R):
            for c in range(C):
                elem = matrix[r][c]
                if elem not in elems:
                    elems[elem] = []
                elems[elem].append((r,c))
        
        ans = [[float('inf')] * C for _ in range(R)]

        prev_r = [0] * R
        prev_c = [0] * C
        for elem in sorted(elems.keys()):
            locs = elems[elem]
            # union find returns a graph where key = node and value = node's parent
            graph = self.helper(locs)
            # print(elem, graph)

            reversed_graph = {}
            for node, parent in graph.items():
                if parent not in reversed_graph:
                    reversed_graph[parent] = []
                reversed_graph[parent].append(node)
            for parent, nodes in reversed_graph.items():
                prev_rank = 0
                for node in nodes:
                    r, c = node
                    prev_rank = max(prev_rank, prev_r[r], prev_c[c])

                rank = prev_rank + 1
                for node in nodes:
                    r, c = node
                    ans[r][c] = rank
                    prev_r[r] = prev_c[c] = rank
        return ans
    
    def helper(self, locs):
        graph = {loc: loc for loc in locs}
        rows = {}
        cols = {}
        for loc in locs:
            r, c = loc
            if r not in rows:
                rows[r] = []
            if c not in cols:
                cols[c] = []
            rows[r].append(loc)
            cols[c].append(loc)
        # print(rows, cols)

        for nodes in rows.values():
            loc1 = nodes.pop()
            while nodes:
                loc2 = nodes.pop()
                self.union(graph, loc1, loc2)
        for nodes in cols.values():
            loc1 = nodes.pop()
            while nodes:
                loc2 = nodes.pop()
                self.union(graph, loc1, loc2)
        for loc in locs:
            graph[loc] = self.find(graph, graph[loc])
        return graph
    
    def union(self, graph, a, b):
        if a > b:
            a, b = b, a
        a_root, b_root = self.find(graph, a), self.find(graph, b)
        graph[b_root] = graph[a_root]
        
    def find(self, graph, a):
        if a != graph[a]:
            graph[a] = self.find(graph, graph[a])
        return graph[a]