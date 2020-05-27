/*
 *  Target Practice 12 - Matrix
 */






'use strict';
//graph traversal, dfs
//time O(4^N)
function robotPaths(matrix) {
  let count = 0
  let xbound = matrix[0].length - 1
  let ybound = matrix.length - 1

  function traverse(x,y) {  //0,0  
    //base cases
    if(x < 0 || y < 0 || x > xbound || y > ybound) {
      return
    }
    if(matrix[y][x] === 1) {
      return
    }
    if(x === xbound && y === ybound) {
      count += 1
      return
    }
    //actions
    //visited
    matrix[y][x] = 1   

/*
[[1,0,0],
 [0,0,0],
 [0,0,0]]

*/
    
    //4 directions
    //Right x+1
    traverse(x+1, y) //1,0
    //Down y+1
    traverse(x, y+1)
    //Left x-1
    traverse(x-1, y)
    //Up y-1
    traverse(x, y-1)
      

 /*
[[0,0,0],
 [0,0,0],
 [0,0,0]]

*/

matrix[y][x] = 0

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