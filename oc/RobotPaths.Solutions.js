/*
 *  Target Practice 12 - Matrix
 */
/*
 *  Problem:  Robot Paths
 *
 *  Prompt:   Given a matrix of zeroes, determine how many unique paths exist
 *            from the top left corner to the bottom right corner
 *
 *  Input:    An Array of Array of Integers (matrix)
 *  Output:   Integer
 *
 *  Example:  matrix = [[0,0,0,0],
 *                      [0,0,0,0],
 *                      [0,0,0,0]]
 *
 *            robotPaths(matrix) = 38
 *
 *
 *            matrix = [[0,0,0],
 *                      [0,0,0]]
 *
 *            robotPaths(matrix) = 4
 *
 *  Note:     From any point, you can travel in the four cardinal directions
 *            (north, south, east, west). A path is valid as long as it travels
 *            from the top left corner to the bottom right corner, does not go
 *            off of the matrix, and does not travel back on itself
 */
'use strict';

function robotPaths(matrix) {
  let rMax = matrix.length - 1
  let cMax = matrix[0].length - 1
  let count = 0
  //graph dfs Time O(4^Area)
  function traverse(row,col) {
    //3 base cases
    //out of bounds
    if(row < 0 || col < 0 || row > rMax || col > cMax) return
    //visited 
    let val = matrix[row][col]
    if(val === 1) return
    //target reached
    if(row === rMax && col === cMax) {
      count++
      return
    }

    //mark visited
    matrix[row][col] = 1
    //traverse in 4 dirs
    traverse(row, col + 1)
    traverse(row, col - 1)
    traverse(row + 1, col)
    traverse(row - 1, col)
    //reset visited
    matrix[row][col] = 0

  }
  traverse(0,0)
  return count

}



////////////////////////////////////////////////////////////
///////////////  DO NOT TOUCH TEST BELOW!!!  ///////////////
////////////////////////////////////////////////////////////

console.log('Robot Paths Tests');
let testCount = [0, 0];

assert(testCount, 'should work on first example input', function(){
  let test = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]];
  var example = robotPaths(test);
  return example === 38;
});

assert(testCount, 'should work on second example input', function(){
  let test = [[0,0,0],
              [0,0,0]];
  var example = robotPaths(test);
  return example === 4;
});

assert(testCount, 'should work on single-element input', function(){
  let test = [[0]];
  var example = robotPaths(test);
  return example === 1;
});

assert(testCount, 'should work on single-row input', function(){
  let test = [[0,0,0,0,0,0]];
  var example = robotPaths(test);
  return example === 1;
});

assert(testCount, 'should work on single-column input', function(){
  let test = [[0],
              [0],
              [0],
              [0],
              [0]];
  var example = robotPaths(test);
  return example === 1;
});

assert(testCount, 'should work on a 5 x 8 matrix input', function(){
  let test = [[0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0],
              [0,0,0,0,0,0,0,0]];
  console.log("  Please be patient, test 6 may take longer to run");
  var example = robotPaths(test);
  return example === 7110272;
});

console.log('PASSED: ' + testCount[0] + ' / ' + testCount[1], '\n\n');



// custom assert function to handle tests
// input: count {Array} - keeps track out how many tests pass and how many total
//        in the form of a two item array i.e., [0, 0]
// input: name {String} - describes the test
// input: test {Function} - performs a set of operations and returns a boolean
//        indicating if test passed
// output: {undefined}
function assert(count, name, test) {
  if (!count || !Array.isArray(count) || count.length !== 2) {
    count = [0, '*'];
  } else {
    count[1]++;
  }

  let pass = 'false';
  let errMsg = null;
  try {
    if (test()) {
      pass = ' true';
      count[0]++;
    }
  } catch(e) {
    errMsg = e;
  }
  console.log('  ' + (count[1] + ')   ').slice(0,5) + pass + ' : ' + name);
  if (errMsg !== null) {
    console.log('       ' + errMsg + '\n');
  }
}

