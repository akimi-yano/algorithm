
"""
arr: 1 meeting room with times booked
left start
right end - inclusive
non-empty - and always valid (chronological)

meeting:
left start
rigth end - inclusive
non-empty 

check if we can book a meeting
if overlap = > return False - cannot book the meeting
else => return True


arr 1 ex
start<30<end
arr 2 ex
start<31<end
start<40<end

meeting=[start,end]
arr = [[29, 30],[31, 40],[60, 75]]
meeting = [28, 50]
# output: False


valid case
arr = [[29, 30],[31, 40],[60, 75]]
meeting = [50, 59]
input: True
"""
def can_book_meeting(arr,meeting):
    start,end = meeting
    low = 0
    high = len(arr)-1
# compare the start with arr[mid][1]
    while low<=high:
        mid = (low+high)//2
        if start<=arr[mid][1]:
            break
        else: 
            low = mid+1

    if start<=arr[mid][1] and end<=arr[mid][0]:
        return False
    else:
        return True      
print(can_book_meeting([[29, 30],[31, 40],[60, 75]],[28, 50]))
# O(n) -> arr[i][1] < meeting[0] -> meeting[1] < arr[i+1][0]
# O(log n) -> arr[i][1] < meeting[0] -> meeting[1] < arr[i+1][0]
# edge cases are for beginning and end of arr
# if i is len(arr) - 1 -> if it passes arr[i][1]<meeting[0] append is valid
# if i is 0 meeting[1] < arr[i][0] ? prepend is valid
# ---------------------------------------------------
# arr = [1,2,3,4,5,4,3,2] -> find the point of inflection
#       --------> <------
# increases and then decreases -> always
# O(n) -> immediately failed
# O(log n) -> 
# unsorted -> sort data? -> think about binary search


# --------------------------------------
# Tic Tac Toe

# class GameBoard():
#   def __init__(self, p1, p2):
#     self.arr = [
#       [0,0,0],
#       [0,0,0],
#       [0,0,0]
#     ]
#     self.turn = 1
#     self.p1 = p1
#     self.p2 = p2
    
#   def win():
#     reference = {
#       "XXX" or "OOO"
#     #   -> X wins, O wins
#     }
  
#   def move(self, player, coords):
#     self.turn -> 1 
#     # check and validate ...
#     self.arr[coords.x, coords.y] = self.turn
#     self.turn = 2
    
  
# class Player():
#   def __init__(self, name):
#     self.name = name

# p1 = Player("Akimi")
# p2 = Player("Pete")
# gb = GameBoard(p1, p2)
# print("Player Akimi goes first")
# move()
# win()
# print(f"{p1.name} wins")

# MineSweeper -> 
# BattleShip -> 











