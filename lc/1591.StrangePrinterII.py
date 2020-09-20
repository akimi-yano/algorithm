# 1591. Strange Printer II
# Hard

# 18

# 0

# Add to List

# Share
# There is a strange printer with the following two special requirements:

# On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.
# Once the printer has used a color for the above operation, the same color cannot be used again.
# You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the position (row, col) of the grid.

# Return true if it is possible to print the matrix targetGrid, otherwise, return false.



# Example 1:



# Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
# Output: true
# Example 2:



# Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
# Output: true
# Example 3:

# Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
# Output: false
# Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.
# Example 4:

# Input: targetGrid = [[1,1,1],[3,1,3]]
# Output: false


# Constraints:

# m == targetGrid.length
# n == targetGrid[i].length
# 1 <= m, n <= 60
# 1 <= targetGrid[row][col] <= 60


# This approach does not work - remember they are layered !

# class Solution:
#     all_colors = set([i for i in range(1,61)])
#     def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
#         def helper(row, col, m, n, color):
#             if not 0<=row<=m-1 or not 0<=col<=n-1 or targetGrid[row][col]!=color:
#                 return 
#             targetGrid[row][col] = 0
#             helper(row+1,col, m, n, color)
#             helper(row-1,col, m, n, color)
#             helper(row,col+1, m, n, color)
#             helper(row,col-1, m, n, color)
            
        
#         m = len(targetGrid)
#         n = len(targetGrid[0])
#         # print(Solution.all_colors)
#         for row in range(m):
#             for col in range(n):
#                 if targetGrid[row][col] in Solution.all_colors:
#                     Solution.all_colors.remove(targetGrid[row][col])
#                     helper(row, col, m, n, targetGrid[row][col])
                    
#         for row in range(m):
#             for col in range(n):
#                 if targetGrid[row][col]!= 0:
#                     return False
#         return True



# THIS SOLUTION WORKS AND INTUITIVE !!!:
class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        '''
        directed graph problem to find if there is cycle
        '''
        m = len(targetGrid)
        n = len(targetGrid[0])
        # check the range of each color and save the info in the dictionary
        colors = {}
        for row in range(m):
            for col in range(n):
                if targetGrid[row][col] not in colors:
                    # start_row, end_row,  start_col, end_col
                    colors[targetGrid[row][col]] = [row,row,col,col]
                else:
                    # start_row
                    colors[targetGrid[row][col]][0] = min(colors[targetGrid[row][col]][0],row)
                    # end_row
                    colors[targetGrid[row][col]][1] = max(colors[targetGrid[row][col]][1],row)
                    # start_col
                    colors[targetGrid[row][col]][2] = min(colors[targetGrid[row][col]][2],col)
                    # end_col
                    colors[targetGrid[row][col]][3] = max(colors[targetGrid[row][col]][3],col)
        # print(colors)
        # make an adjecency list (use set to remove dups) by looping through dictionary and the row & col range - its fine because there are only about 60 colors, rows and cols each at max
        adj_list = {}
        for color, pos in colors.items():
            start_row, end_row,  start_col, end_col = pos
            for row in range(start_row, end_row+1):
                for col in range(start_col, end_col+1):
                    if targetGrid[row][col] != color:
                        if color not in adj_list:
                            adj_list[color] = set([targetGrid[row][col]])
                        else:
                            adj_list[color].add(targetGrid[row][col])
        # print(adj_list)
        # check if there is cycle by using seen set
        def is_cycle(cur):
            if cur in seen:
                return True
            if cur not in adj_list:
                return False

            seen.add(cur)
            
            for next_node in adj_list[cur]:
                if is_cycle(next_node):
                    return True
            # back track if its False - remove from the set before returning
            seen.remove(cur)
            return False
            
        seen = set([])
        for node in adj_list:
            if is_cycle(node):
                return False
        return True
            
        