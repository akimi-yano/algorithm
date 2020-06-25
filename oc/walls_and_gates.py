# https://leetcode.com/problems/walls-and-gates/
# given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle.
# 0 - A gate.
# INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may 
# assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, 
# it should be filled with INF.

# Example: 

# Given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

####PREMIUM ---

##### the code below is broken:


# grid = [[2147483647,-1,0,2147483647],
# [2147483647,2147483647,2147483647,-1],
# [2147483647,-1,2147483647,-1],
# [0,-1,2147483647,2147483647]]



# -1 - A wall or an obstacle.
# 0 - A gate.


def nearest_gates(rooms):
  def dfs(i, j, dist):
    if i<0 or j<0 or i>= len(rooms) or j >= len(rooms[i]) or rooms[i][j] == -1 or rooms[i][j] == 0:
        return 
    
    if dist < rooms[i][j]:
      rooms[i][j] = dist
        
      for p, q in [(i+1,j), (i-1, j), (i, j-1), (i, j+1)]:
        dfs(p,q, dist+1)
          
  for i in range(len(rooms)):
      for j in range(len(rooms[0])):
          if rooms[i][j] == 0:
              dfs(i+1,j,1)
              dfs(i-1,j,1)
              dfs(i,j-1,1)
              dfs(i,j+1,1)
  return rooms
                  
rooms = [[2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]]
  
# expected answer: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
print(nearest_gates(rooms))
