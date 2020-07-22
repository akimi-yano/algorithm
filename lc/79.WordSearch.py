# 79. Word Search
# Medium

# 3885

# 190

# Add to List

# Share
# Given a 2D board and a word, find if the word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example:

# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]

# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
 

# Constraints:

# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3


# yay this works !
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def helper(r,c,i,word):
            if i>len(word)-1:
                return True
            if r<0 or c<0 or r>len(board)-1 or c>len(board[0])-1:
                return False
            # print(r,c,i,word)
            
            right = left = up = down = False
            if word[i] == board[r][c]:
                temp = board[r][c]
                board[r][c]= "#"
                right = helper(r+1,c,i+1,word)
                left = helper(r-1,c,i+1,word)
                up = helper(r,c+1,i+1,word)
                down = helper(r,c-1,i+1,word)
                res = right or left or up or down
                if not res:
                    board[r][c] = temp
            return right or left or up or down

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col]==word[0]:
                    if helper(row,col,0,word):
                        return True
        return False
    
    
# this works and faster
def exist(self, board, word):
    if not board:
        return False
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            if self.dfs(board, i, j, word):
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    tmp = board[i][j]  # first character is found, check the remaining part
    board[i][j] = "#"  # avoid visit agian 
    # check whether can find "word" along one direction
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
    board[i][j] = tmp
    return res