// Depth First Traversals
// (a) Inorder (Left, Root, Right) 
// (b) Preorder (Root, Left, Right) 
// (c) Postorder (Left, Right, Root) 
// InOrder Traversal example
// function InorderTraversal(current){
//     if(current == null){
//       return;
//     }
//     console.log(current.val);
//     InorderTraversal(current.left);
//     InorderTraversal(current.right);
//   }
  // Create standalone or class methods that traverse binary search trees and print all their nodes.
  // Challenge 2: Create class methods that create arrays of node values and return them, Inorder, Preorder, and Postorder.
  // Hint: These methods are very very similiar to one another. It just depends on where you print or .push, and where your function calls are.


class BinaryNode {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}
class BST {
    constructor() {
        this.root = null;
    }
    insert(val, current) {
        if (this.root == null) {
            this.root = new BinaryNode(val);
            return this;
        }
        if (!current) {
            current = this.root;
        }
        if (val > current.val && current.right != null) {
            this.insert(val, current.right);
        }
        if (val > current.val && current.right == null) {
            current.right = new BinaryNode(val);
        }
        if (val < current.val && current.left != null) {
            this.insert(val, current.left);
        }
        if (val < current.val && current.left == null) {
            current.left = new BinaryNode(val);
        }
        return this;
    }

    inorder(current) {
        if (current ==null){
            return
        }
        this.inorder(current.left)
        console.log(current.val)
        this.inorder(current.right)
    }
    preorder(current) {
        if (current ==null){
            return
        }
        console.log(current.val)
        this.preorder(current.left)
        this.preorder(current.right)
    }
    postorder(current) {
        if (current ==null){
            return
        }
        this.postorder(current.left)
        this.postorder(current.right)
        console.log(current.val)
    }
    inorderArr(current, arr) {
        if (!arr){arr=[]}
        if (current ==null){
            return arr
        }
        this.inorderArr(current.left, arr)
        arr.push(current.val)
        this.inorderArr(current.right, arr)
        return arr
    }
    preorderArr(current,arr) {
        if (!arr){arr=[]}
        if (current ==null){
            return arr
        }
        arr.push(current.val)
        this.preorderArr(current.left, arr)
        this.preorderArr(current.right, arr)
        return arr
    }
    postorderArr(current, arr) {
        if (!arr){arr=[]}
        if (current ==null){
            return arr
        }
        this.postorderArr(current.left, arr)
        this.postorderArr(current.right, arr)
        arr.push(current.val)
        return arr
    }

}
let tree = new BST();
tree.insert(66).insert(55).insert(99).insert(44).insert(60);
console.log(tree.root.left.left);
console.log(tree)

console.log("INORDER")
tree.inorder(tree.root)

console.log("PREORDER")
tree.preorder(tree.root)

console.log("POSTORDER")
tree.postorder(tree.root)

console.log("INORDERARR")
console.log(tree.inorderArr(tree.root))

console.log("PREORDERARR")
console.log(tree.preorderArr(tree.root))

console.log("POSTORDERARR")
console.log(tree.postorderArr(tree.root))



