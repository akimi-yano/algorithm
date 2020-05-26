// 37. Sudoku Solver
const input = [
    [5, 3, 1,   0, 7, 0,   0, 0, 0],
    [6, 0, 0,   1, 9, 5,   0, 0, 0],
    [0, 9, 8,   0, 0, 0,   0, 6, 0],

    [8, 0, 0,   0, 6, 0,   0, 0, 3],
    [4, 0, 0,   8, 0, 3,   0, 0, 1],
    [7, 0, 0,   0, 2, 0,   0, 0, 6],

    [0, 6, 0,   0, 0, 0,   2, 8, 0],
    [0, 0, 0,   4, 1, 9,   0, 0, 5],
    [0, 0, 0,   0, 8, 0,   0, 7, 9]
]
zeroCoords = []; //[[0,3], [0,5], ...]
input.forEach((row, x) => {
    row.forEach((el, y) => {
        if (el === 0)
            zeroCoords.push([x, y]);
    })
})
console.log(zeroCoords.length)
let results;
// [1,2,3]  start= 0 - 1 ,  2,  3
// let counter = 0; 
const solver = (start) => {
//   counter++
    if(start === zeroCoords.length)
      console.log(input);
    //   console.log(counter); 
      return;
    for(let j=1;j<=9;j++){
      const [x,y] = zeroCoords[start]; 
      if(canPlace(x,y,j)){
        input[x][y] = j; 
        solver(start+1); ///---------------
        input[x][y] = 0;
      }
    }
}

const canPlace = (x, y, num) => {
    for (let row = 0; row < 9; row++) { //row check   //9 sets
        if (input[row][y] === num) return false;  
    }
    for (let col = 0; col < 9; col++) {//col check  //9 sets
        if (input[x][col] === num) return false;
    }
    //grid check
    boxIndex=x/3*3+y*3
    const blockXStart = Math.floor(x / 3) * 3;
    const blockYStart = Math.floor(y / 3) * 3;
    for (let blockX = blockXStart; blockX < blockXStart + 3; blockX++) { //9 sets
        for (let blockY = blockYStart; blockY < blockYStart + 3; blockY++) {
            if (input[blockX][blockY] === num) return false;
        }
    }
    return true;
}

solver(0); 

//iterate through all zeroes
  //try 1-9 on each one, if we can place
    //move to next
  

//Validate Row, Column, and Grid