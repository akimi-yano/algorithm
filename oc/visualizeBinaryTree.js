
// DO NOT EDIT
// Node class for a binary tree node
class TreeNode {
  constructor(value){
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// DO NOT EDIT
// generate tree from array
function deserialize(arr) {
  if (arr.length === 0) { return null; }
  let root = new TreeNode(arr[0]);
  let queue = [root];
  for(let i = 1; i < arr.length; i += 2) {
    let current = queue.shift();
    if (arr[i] !== null) {
      current.left = new TreeNode(arr[i]);
      queue.push(current.left);
    }
    if (arr[i + 1] !== null && arr[i + 1] !== undefined) {
      current.right = new TreeNode(arr[i + 1]);
      queue.push(current.right);
    }
  }
  return root;
}





/*

 *
 *              4
 *            /   \
 *          2        6
 *        /   \    /   \
 *      1       3 5     7
 * 
 *                  

[4,2,6,1,3,5,7]

                   4
                /     
              2
            /   \
           1     3
           
[4,2,null,1,3]

                      4
                    /
                  3
                /
              2
            /
          1

[4,3,null,2,null,1,null]

 */


 // DO NOT EDIT
// const arr = [4, 2, 6, 1, 3, 5, 7, 1, 1, 1, 1, 1, 1, 1, 1];
const arr = [4, 2, 6, 1, null, 5, 7, 1, 1, 1, null, 1, 1];
// const arr = [4, 2, 6, 1, 3, 5, 7];
// const arr = [4, 2, 6];
// const arr = [4];

const sampleTree = deserialize(arr);

// console.log(sampleTree);

/*

Considerations: 

* Work with only single digit numbers

*/


function visualizeTree(root) {
  // traverse through tree and find depth of tree
  let treeHeight = getHeight(root);
  
  // console.log("TREE HEIGHT: ", treeHeight);
  
  // Create matrix of appropriate dimensions
  // insert empty spaces
  // height of matrix is 2 * treeHeight - 1
  // width is 2^(h-1) + 3 * (2^(h-1) - 1)
  
  let matrixHeight = 2 * treeHeight - 1;
  let matrixWidth = Math.pow(2, treeHeight - 1) + 3 * (Math.pow(2, treeHeight - 1) - 1);
  
  // console.log("MATRIX HEIGHT: ", matrixHeight);
  // console.log("MATRIX WIDTH: ", matrixWidth);
  
  const matrix = [];
  for (let i = 0; i < matrixHeight; i++) {
    matrix.push(new Array(matrixWidth).fill(" ")); 
  }
  
  printMatrix(matrix);
  
  // recursively travel through tree

  function traverse(current, treeDepth, matrixDepth, matrixIndex, type) {
    if (current === null) {
      return;
    }
    
    // even index, insert node value
    if (matrixDepth % 2 === 0) {
      matrix[matrixDepth][matrixIndex] = current.value;
      
      traverse(current.left, treeDepth, matrixDepth + 1, matrixIndex - 2 ** (treeHeight - treeDepth - 2), "left");
      traverse(current.right, treeDepth, matrixDepth + 1, matrixIndex + 2 ** (treeHeight - treeDepth - 2), "right");
    }
    
    // odd index, insert slash
    if (matrixDepth % 2 === 1) {
      if (type === "left") {
        matrix[matrixDepth][matrixIndex] = "/";
        traverse(current, treeDepth + 1, matrixDepth + 1, matrixIndex - 2 ** (treeHeight - treeDepth - 2), "left");
      } else if (type === "right") {
        matrix[matrixDepth][matrixIndex] = "\\";        
        traverse(current, treeDepth + 1, matrixDepth + 1, matrixIndex + 2 ** (treeHeight - treeDepth - 2), "left");        
      }
    }
    
    
    // when calling recursively, travel over 2 ^ n
  }
  
  traverse(root, 0, 0, Math.floor(matrixWidth / 2), null)
  
  console.log('');
  printMatrix(matrix);
}

visualizeTree(sampleTree);

function printMatrix(matrix) {
  console.log("THE DIAGRAM");
  for (let row of matrix) {
    console.log(row.join(''));
  }
}

function getHeight(root) {
  let maxDepth = 0;
  
  function traverse(current, depth) {
    if (current === null) {
      return;
    }
    
    maxDepth = Math.max(maxDepth, depth);
    
    traverse(current.left, depth + 1);
    traverse(current.right, depth + 1);
  }
  
  traverse(root, 1);
  return maxDepth;
}

