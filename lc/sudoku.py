class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check horizontally
        for i in range(9):
            memo = set([])
            for k in range(9):
                if board[i][k] == '.':
                    continue
                elif board[i][k] in memo:
                    return False
                else:
                    memo.add(board[i][k])
                    
        # check vertically
        for j in range(9):
            memo = set([])
            for s in range(9):   
                if board[s][j] == '.':
                    continue
                elif board[s][j] in memo:
                    return False
                else:
                    memo.add(board[s][j])
        
        # check inside boxes
        for k in range(9):
            memo = set([])
            x_offset = (k % 3) * 3
            y_offset = (k // 3) * 3
            for x in range(3):
                for y in range(3):
                    num = board[x+x_offset][y+y_offset]
                    if num == '.':
                        continue
                    elif num in memo:
                        return False
                    else:
                        memo.add(num)
        
        return True


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         # check horizontally
#         for i in range(9):
#             memo = set([])
#             for k in range(9):
#                 if board[i][k] == '.':
#                     continue
#                 elif board[i][k] in memo:
#                     return False
#                 else:
#                     memo.add(board[i][k])
            
                    
#         # check vertically
#         for j in range(9):
#             memo = set([])
#             for s in range(9):   
#                 if board[s][j] == '.':
#                     continue
#                 elif board[s][j] in memo:
#                     return False
#                 else:
#                     memo.add(board[s][j])
#                 print(memo)
            
#         # Use %3 because its 3 x 3
        
#         # 1,3 *  1,3 - 3,6 - 6,9 
#         # 3,6
#         # 6,9
#         memo = set([])
#         for t in range(0,3):
#             for p in range(0,3):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
        
#         memo = set([])
#         for t in range(0,3):
#             for p in range(3,6):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
#         memo = set([])
#         for t in range(0,3):
#             for p in range(6,9):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
#         memo = set([])
#         for t in range(3,6):
#             for p in range(0,3):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
#         memo = set([])
#         for t in range(3,6):
#             for p in range(3,6):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
#         memo = set([])
#         for t in range(3,6):
#             for p in range(6,9):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
#         memo = set([])
#         for t in range(6,9):
#             for p in range(0,3):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
#         memo = set([])
#         for t in range(6,9):
#             for p in range(3,6):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
                    
#         memo = set([])
#         for t in range(6,9):
#             for p in range(6,9):
#                 if board[t][p] == '.':
#                     continue
#                 elif board[t][p] in memo:
#                     return False
#                 else:
#                     memo.add(board[t][p])
        
#         return True