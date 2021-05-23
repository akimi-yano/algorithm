# 51. N-Queens
# Hard

# 3189

# 111

# Add to List

# Share
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

# Example 1:


# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:

# Input: n = 1
# Output: [["Q"]]
 

# Constraints:

# 1 <= n <= 9

# This solution works:

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        def helper(queens, available_columns):
            nonlocal ans, n
            if len(queens) == n:
                board = [['.'] * n for _ in range(n)]
                for r, c in queens:
                    board[r][c] = 'Q'
                ans.append([''.join(row) for row in board])
                return
            
            start_row = queens[-1][0]+1 if queens else 0
            for r in range(start_row, n):
                for c in list(available_columns):
                    if all(abs(r-qr) - abs(c-qc) != 0 for (qr, qc) in queens):
                        available_columns.remove(c)
                        queens.append((r, c))
                        helper(queens, available_columns)
                        queens.pop()
                        available_columns.add(c)

        helper([], set([c for c in range(n)]))
        return ans
