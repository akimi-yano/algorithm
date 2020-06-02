
# matrix 
def spiral(num):
  # create matrix 
  # edge cases
  if num <= 0: return []
  
  matrix = [[0]*(num) for i in range(num)]
  min_row, min_col = 0,0
  max_row, max_col = num-1, num-1
  counter = 1
  
  while min_row <= max_row and min_col <= max_col:
    # first row 
    for c in range(min_col, max_col+1):
      matrix[min_row][c] = counter
      counter+= 1
    min_row += 1
    
    # last col
    for r in range(min_row, max_row+1):
      matrix[r][max_col] = counter
      counter += 1
    max_col -= 1
    
    # last row 
    for c in range(max_col, min_col-1, -1):
      matrix[max_row][c] = counter
      counter += 1
    max_row -= 1
    
    # first col
    for r in range (max_row, min_row-1, -1):
      matrix[r][min_col] = counter
      counter +=1
    min_col += 1
    
  return matrix
  


print(spiral(3))
print(spiral(1)) #[[1]]


    
    
  












