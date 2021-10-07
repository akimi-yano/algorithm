# 79. Word Search
# Medium

# 7015

# 274

# Add to List

# Share
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

# Example 1:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
 

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
 

# Follow up: Could you use search pruning to make your solution faster with a larger board?


# This solution works:


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def helper(row, col, i):
            if not(0<=row<ROW) or not(0<=col<COL):
                return False
            if i == len(word)-1:
                if board[row][col] == word[i] and (row, col) not in seen:
                    return True
                else:
                    return False
            
            if board[row][col] == word[i] and (row, col) not in seen:
                seen.add((row, col))
                if helper(row+1, col, i+1):
                    return True
                if helper(row-1, col, i+1):
                    return True
                if helper(row, col+1, i+1):
                    return True
                if helper(row, col-1, i+1):
                    return True
                seen.remove((row, col))
            return False
        
        ROW = len(board)
        COL = len(board[0])
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == word[0]:
                    seen = set([])
                    if helper(row, col, 0):
                        return True
        return False
