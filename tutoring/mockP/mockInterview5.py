

"""

[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]

"""
arr = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

arr = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12],
  [13,14,15,16]
]    

# def rotate(array): 
#   # switching row and columns
#   for row in range(len(array)):
#     for col in range(row,len(array[row])):
#       array[row][col],array[col][row]=array[col][row],array[row][col]
#   # switching rows left to right
#   for j in range(len(array)):
#     for i in range(len(array[j])//2):
#       array[j][i],array[j][len(array[j])-1-i]=array[j][len(array[j])-1-i],array[j][i]
#   return array
# print(rotate(arr))
# temp = 2
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]


# [
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
#   [x,x,x,x,x,x,x,x,x,x,x,x],
  
# ]

# [
#   [x,x,x,x],
#   [x,x,x,x],
#   [x,x,x,x],
#   [x,x,x,x],
# ]

# [
#   [x,x,x],
#   [x,x,x],
#   [x,x,x],
# ]

#  0 len(row) - 1
#  1 len(row) - 1 - i
def rotate(array):
  for row in range(len(array) // 2):
    for col in range(row, len(array[row]) - row - 1):
      col_inverse = len(array[row]) - col - 1
      row_inverse = len(array[row]) - row - 1
      temp = array[row][col]
      array[row][col] = array[col_inverse][row]
      array[col_inverse][row] = array[row_inverse][col_inverse]
      array[row_inverse][col_inverse] = array[col][row_inverse]
      array[col][row_inverse] = temp
      
      arr = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
      temp = array[row][col]
      array[row][col] = array[col][row_inverse]
      array[col][row_inverse] = array[row_inverse][col_inverse]
      array[row_inverse][col_inverse] = array[col_inverse][row]
      array[col_inverse][row] = temp
      
      
#       temp = array[row][col]
#       array[row][col] = array[3][0]
#       array[3][0] = array[3][3]
#       array[3][3] = array[0][3]
#       array[0][3] = temp
      
#       temp = array[row][col]
#       array[row][col] = array[2][0]
#       array[2][0] = array[3][2]
#       array[3][2] = array[1][3]
#       array[1][3] = temp
      
#       temp = array[row][col]
#       array[row][col] = array[1][0]
#       array[1][0] = array[3][1]
#       array[3][1] = array[2][3]
#       array[2][3] = temp
  return array
# temp = 6
# [
#   [13,9,5,1],
  
#   [14, 6, 7,  2],
#   [15, 10,11, 3],
  
#   [16,12,8,4]
# ]     
      
      # temp = array[row][col]
      # array[row][col] = array[2][0]
      # array[2][0] = array[2][2]
      # array[2][2] = array[0][2]
      # array[0][2] = temp
      
      # temp = array[row][col]
      # array[row][col] = array[1][0]
      # array[1][0] = array[2][1]
      # array[2][1] = array[1][2]
      # array[1][2] = temp
print(rotate(arr))



# def rotate(array):
#   temp = []
#   for col in range(len(array[0])):
#     t = []
#     for row in range(len(array)-1,-1,-1):
#       t.append(array[row][col])
#     temp.append(t)
#   return temp 
# print(rotate(arr))

# define a function that will take an array and n as
# an input. 1 <= n <= 4
# rotate the array clockwise n number of times
# and return the original array

def rotate(array, n):
  if n == 4:
    return array
  if n == 3:
    #reverse
    pass
  if n == 2:
    # rotate twice or rotate with different parameters
    pass
  if n == 1:
    #rotate normally
    pass
  pass


def findLargestSlice(cake_array, participants):
  # cake_array has radii e.g. [3,2,3,1...]
  # sort array largest to smallest
  
  # 3.14.....
  # find the largest equal slice you can make
  # across differing cake slices for the # of participants
  pass




