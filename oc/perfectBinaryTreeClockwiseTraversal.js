let tree =
{
"value": "a",
"left": {
"value": "g",
"left": {
"value": "m",
"left": {
"value": "f",
"left": null,
"right": null
},
"right": {
"value": "c",
"left": null,
"right": null
}
},
"right": {
"value": "p",
"left": {
"value": "s",
"left": null,
"right": null
},
"right": {
"value": "r",
"left": null,
"right": null
}
}
},
"right": {
"value": "w",
"left": {
"value": "u",
"left": {
"value": "t",
"left": null,
"right": null
},
"right": {
"value": "o",
"left": null,
"right": null
}
},
"right": {
"value": "z",
"left": {
"value": "k",
"left": null,
"right": null
},
"right": {
"value": "x",
"left": null,
"right": null
}
}
}
}


/*

For this task, you will be given the elements of a perfect binary tree of
 characters, stored within a simple tree data structure.

Your goal is to write a function that starts at the root of the 
tree and returns a counter clockwise traversal of the nodes at the 
edge of the tree.

1. Undrestanding 
- Input/output, ask for example, come up with your own example 
- Constrains
2. Diagram 
3. Sudocode 
4. Code 


input:

             a
           /   \
         g       w
        / \     / \
       m   p   u    z
      / \ / \ / \  / \
     f  c s r t  o k  x
     
Output:  [a, g, m, f, c, s, r, t, o, k, x, z, w]

constrains: 
- only edges 
- perfect binary tree: every non-leaf node has exactly 2 children 

input:
             a   
           /   \
         g       w

      
output: [a, g, w]


Diagraming: 
split the problem

             a
           /   \
         g       w
        / \     / \
       m   p   u    z
      / \ / \ / \  / \
     f  c s r t  o k  x
     
Left 
add to the result array 
traverse to the left node 

children 
go through the full tree
if a leave is a child add it to result array 

right 
traverse to the next node 
add to the result array 


*/

// bruteforce 
function traverseLeft(root, result){
  //base case 
  if(!root.left){
    return result
  }
  
  // recursive case 
  result.push(root.value)
  return  traverseLeft(root.left, result)
}

function traverseChildren(root, result){
  //base case 
  if(!root.left){
    result.push(root.value)
    return result
  }
  // recursive case 
  traverseChildren(root.left, result)
  traverseChildren(root.right, result)
  return result
}

function traverseRight(root, result){
  // base case 
  if(!root.right){
    return result
  }
  //recursive case 
  traverseRight(root.right, result)
  result.push(root.value)
  return result
}


function counterClock(root){
  let result = []
  result.push(root.value)
  result.push(...traverseLeft(root.left, []))
  result.push(...traverseChildren(root, []))
  result.push(...traverseRight(root.right, []))
  return result
}


function counterClockTwo(root){
  let result = []
  
  function traverse(root, left, right){
    // leaves 
    if(!root.left){
      result.push(root.value)
      return
    }
    // pre order = left
    if(left){
      result.push(root.value)
    }
    traverse(root.left, left, false)
    traverse(root.right, false, right)
    
    // right
    if(right &&!left){
      result.push(root.value)
    }
    
  }
  traverse(root, true, true)
  
  return result
}




console.log(counterClockTwo(tree))
















