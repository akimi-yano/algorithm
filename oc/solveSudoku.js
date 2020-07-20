// Solving Sudoku with Backtracking

const input = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

const emptySpaces = []
input.forEach((row,x) =>{
  row.forEach((el,y) =>{
    if(el === 0){
      emptySpaces.push([x,y])
    }
  })
})//[  [0,2], [0,3]....[1,1]  ....  ]

const canPlace = (x,y,num,arr)=>{
  for(let row = 0; row < 9; row++){
    if(arr[row][y] === num) return false
  }
  for(let col = 0; col < 9; col++){
    if(arr[x][col] === num) return false
  }
  // 0 1 2 3 4 5 6 7 8
  // 0 0 0 3 3 3 6 6 6
  const blockXStart = Math.floor(x / 3) * 3;
  const blockYStart = Math.floor(y / 3) * 3;
  for (let blockX = blockXStart; blockX < blockXStart + 3; blockX++) {
        for (let blockY = blockYStart; blockY < blockYStart + 3; blockY++) {
            if (arr[blockX][blockY] === num) return false;
        }
    }
  return true; 
}

const solve = (index, arr)=>{
  if(index == emptySpaces.length){
    console.log(arr)
    return
  }
  const [x,y] = emptySpaces[index]; 
  for(let i = 1; i <= 9; i++){
    if(canPlace(x,y,i,arr)){
      arr[x][y] = i
      solve(index+1, arr)
      arr[x][y] = 0
    }
  }
}
      //spot 1 -  2
        //spot 2 - 1




solve(0, input) 