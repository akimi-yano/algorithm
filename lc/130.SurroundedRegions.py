# 130. Surrounded Regions
# Dont copy - dont work
#  class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         """
#         Do not return anything, modify board in-place instead.
#         """
#         dont_flip = set([])
#         def check(row,col):
#             if row<0 or col<0 or row>len(board)-1 or col>len(board[0])-1:
#                 return
#             if board[row][col]=="X":
#                 return 
#             dont_flip.add((row,col))
#             check(row,col-1)
#             check(row,col+1)
#             check(row-1,col)
#             check(row+1,col)
        
#         for i in range(len(board)):
#             if board[0][i] == "O":
#                 check(0,i)
#             if board[len(board)-1][i] == "O":
#                 check(len(board)-1,i)
#             if board[i][0] == "O":
#                 check(i,0)
#             if board[i][len(board)-1] == "O":
#                 check(i,len(board)-1)
        
#         def helper(row,col):
#             if row<0 or col<0 or row>len(board)-1 or col>len(board[0])-1:
#                 return
#             if board[row][col]=="X":
#                 return
#             if (row,col) not in dont_flip:
#                 board[row][col] = "X"
#             helper(row,col-1)
#             helper(row,col+1)
#             helper(row-1,col)
#             helper(row+1,col)
        
#         for row in range(len(board)):
#             for col in range(len(board[row])):
#                 # print(board[row][col])
#                 if board[row][col] == "O":
#                     helper(row,col)


# this doesnt work either
    # def solve(self, board: List[List[str]]) -> None:
    #     """
    #     Do not return anything, modify board in-place instead.
    #     """
    #     def check(row,col):
    #         if row<0 or col<0 or row>len(board)-1 or col>len(board[0])-1:
    #             return
    #         if board[row][col]=="X":
    #             return 
    #         board[row][col]="A"
    #         if col>0:
    #             check(row,col-1)
    #         if col<len(board)-1:
    #             check(row,col+1)
    #         if row>0:
    #             check(row-1,col)
    #         if row<len(board)-1:
    #             check(row+1,col)
        
    #     for i in range(len(board)):
    #         if board[0][i] == "O":
    #             print(0,i)
    #             # check(0,i)
    #         if board[len(board)-1][i] == "O":
    #             check(len(board)-1,i)
    #             print(len(board)-1,i)
    #         if board[i][0] == "O":
    #             check(i,0)
    #             print(i,0)
    #         if board[i][len(board)-1] == "O":
    #             check(i,len(board)-1)
    #             print(i,len(board)-1)
        
    #     for row in range(len(board)):
    #         for col in range(len(board[row])):
    #             if board[row][col] == "O":
    #                 board[row][col] = "X"
        
    #     for row in range(len(board)):
    #         for col in range(len(board[row])):
    #             if board[row][col] == "A":
    #                 board[row][col] = "O"
        
    # this doesnt work either
    # def solve(self, board: List[List[str]]) -> None:
        #   def check(row,col):
        #     if row<0 or col<0 or row>len(board)-1 or col>len(board[0])-1:
        #         return
        #     if board[row][col]=="X":
        #         return 
        #     board[row][col]="A"
        #     if col>0:
        #         check(row,col-1)
        #     if col<len(board)-1:
        #         check(row,col+1)
        #     if row>0:
        #         check(row-1,col)
        #     if row<len(board)-1:
        #         check(row+1,col)
        
        # for i in range(len(board)):
        #     if board[0][i] == "O":
        #         # print(0,i)
        #         check(0,i)
        #     if board[len(board)-1][i] == "O":
        #         check(len(board)-1,i)
        #         # print(len(board)-1,i)
        #     if board[i][0] == "O":
        #         check(i,0)
        #         # print(i,0)
        #     if board[i][len(board)-1] == "O":
        #         check(i,len(board)-1)
        #         # print(i,len(board)-1)
        
        # for row in range(len(board)):
        #     for col in range(len(board[row])):
        #         if board[row][col] == "O":
        #             board[row][col] = "X"
        
        # for row in range(len(board)):
        #     for col in range(len(board[row])):
        #         if board[row][col] == "A":
        #             board[row][col] = "O"

    
    
    # this works
def solve(self, board: List[List[str]]) -> None:
        
     if not board or not board[0]:
            return
        R, C = len(board), len(board[0])
        if R<=2 or C<=2:
            return
        queue = collections.deque()
        for r in range(R):
            queue.append((r, 0))
            queue.append((r, C - 1))

        for c in range(len(board[0])):
            queue.append((0, c))
            queue.append((R - 1, c))

        while queue:
            r, c = queue.popleft()
            print(r, c)
            if 0 <= r < R and 0 <= c < C and board[r][c] == 'O':
                board[r][c] = 'N'
                queue.append((r-1, c))
                queue.append((r + 1, c))
                queue.append((r, c + 1))
                queue.append((r, c - 1))

        for r in range(R):
            for c in range(C):
                if board[r][c] == 'N':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'