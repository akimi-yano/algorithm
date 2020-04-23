class BinaryNode {
    constructor(val) {
        this.val = val
        this.left = null
        this.right = null
    }
}
class BST {
    constructor() {
        this.root = null
    }
}

// console.log(BST.getSmallest())
// console.log(BST.getLargest())
// console.log(BST.searchVal())


// const populate = (arr) => {
//     // creates a binary search tree from the given array
//     this.root = new BinaryNode(arr[0]);
//     for (let i = 1; i < arr.length; i++) {
//         let runner = this.root;
//         while (true) {
//             if (runner.left && arr[i] < runner.val) {
//                 runner = runner.left;
//             } else if (runner.right && arr[i] > runner.val) {
//                 runner = runner.right;
//             } else {
//                 break;
//             }
//         };

//         if (arr[i] < runner.val) {
//             runner.left = new BinaryNode(arr[i]);
//         } else {
//             runner.right = new BinaryNode(arr[i]);
//         }
//     }
// }
// populate()
// BST()

// // console.log(getSmallest(current))
// // // the first time we call getSmallest, pass the root node
// // console.log(getLargest(current))
// // // if there are no nodes at all, return null
// // cnosole.log(findValue(target, current))
// // // current is like runner, it's the current node we're looking at.
// // value is the target, we are always checking value vs current.val to see if we found our node
// // return false if we hit the bottom of our tree without finding the val


// //getSmallest 
// const getSmallest = (node = this.root) => {
//     if (node.left === null) {
//         return node.val;
//     }
//     return getSmallest(node.left)
// }

// const getLargest = (node = this.root) => {
//     if (node.right === null) {
//         return node.val
//     }
//     return getLargest(node.right)
// }

// const findValue = (target, current) => {
//     if (target === current.val) {
//         return true;
//     } else if (current.left === null && current.right === null) {
//         return false;
//     }

//     if (target > current.val) {
//         return findValue(target, current.right);
//     } else {
//         return findValue(target, current.left);
//     }

// }

// function getSmallest(current) {
//     if (current.left === null) {
//       return current;
//     }
//     else {
//       return this.getSmallest(current.left);
//     }
//   }
//   function getLargest(current) {
//     if (current.right === null) {
//       return current;
//     }
//     else {
//       return this.getLargest(current.right);
//     }
//   }
//   function findValue(value, current) {
//     if (value === current) {
//       return true;
//     }
//     else if (value < current) {
//       return this.findValue(value, current.left);
//     }
//     else if (value > current) {
//       return this.findValue(value, current.right);
//     }
//     else {
//       return false;
//     }
//   }
  
  
  
  
  
  
  
  
  
  
  
  