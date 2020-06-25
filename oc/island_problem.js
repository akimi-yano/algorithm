/*
200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and 
'0's (water), count the number of islands. 
An island is surrounded by water and is formed 
by connecting adjacent lands horizontally or 
vertically. You may assume all four edges of 
the grid are all surrounded by water.

Example 1:

Input:
11010
11010
11000
00000

All of your islands is in rectangle shape
O(M+N) O(1)
i=0, j=0, 
no DFS


bottom right corner




Output: 1
Example 2:

Input:
11000
11000
00100
00011

loop throught the matrix, if it is 1 

E.g. 0, 0

Output: 3
*/

// do dfs on every element
// Base case : 1. go out of bounds
// 2. If already visited
// 3. If it's 0 (water)
// Define scape var count to count islands
// Time O(MN) Space O()


matrix1=
[
[1,1,1,1,0],
[1,1,0,1,0],
[1,1,0,0,0],
[0,0,0,0,0]
]


matrix2 = 
[
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]
]





const numberOfIsalnds = (matrix) => {
  if (matrix === undefined || matrix === null) {return 0}
  
  let count = 0
  
  const dfs = (row, col) => {
    if (row < 0 || col < 0 || row >= matrix.length || col >= matrix[0].length) {return}
    if (matrix[row][col] === 0) {return}
    
    matrix[row][col] = 0
    dfs(row + 1, col)
    dfs(row - 1, col)
    dfs(row, col + 1)
    dfs(row, col - 1)
  }
  
  
  
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (matrix[i][j] === 1) {
        count++
        dfs(i, j)
      }
    }
  }
  return count
}

const matrix = undefined

console.log(numberOfIsalnds(matrix1)) //should return 1
console.log(numberOfIsalnds(matrix2)) //should return 3











