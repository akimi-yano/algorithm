//http://btv.melezinek.cz/binary-search-tree.html
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
//getSmallest 
// getSmallest (node = this.root){
//     if (node.left === null) {
//         return node.val;
//     }
//     return getSmallest(node.left)
// }

// getLargest(node = this.root) {
//     if (node.right === null) {
//         return node.val
//     }
//     return getLargest(node.right)
// }

// findValue(target, current) {
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
isEmpty(){
    return this.root===null;
}
// return boolean

getMin(){
    if (this.root===null){
        return false}
    let current = this.root;
    while (current.left !== null){
        current = current.left
    }
    return current.val
}
// return the minimum value in this tree

getMax(){
    if (this.root===null){
        return false}
    let current = this.root;
    while (current.right !== null){
        current = current.right
    }
    return current.val
}
// return maximum value in this tree

recursiveGetMin(node = this.root){
    if (node.left=== null){
        return node.val
    }
    return this.recursiveGetMin(node.left)
}

// return the max value of a given tree
// do not iteratively traverse your tree

// if(!node){
//     node = this.root;
// }

recursiveGetMax(node = this.root){
    if (node.right=== null){
        return node.val
    }
    return this.recursiveGetMax(node.right)

}
// return the max value of a given tree
// do not iteratively traverse your tree
deleteMin(){
    if (this.root===null){
        return false}
    let current = this.root;
    let next =this.root.left;
    
    while (next.left !== null){
        current = next;
        next = next.left;
    }
    // current.left = null; will  break if there is children 
    current.left = next.right;
    return this;
}
deleteMax(){
    if (this.root===null){
        return false}
    let current = this.root;
    let next =this.root.right;
    while (next.right !== null){
        current = next;
        next = next.right;
    }
    // current.right = null; will  break if there is children 
    current.right = next.left;
    return this;
}
}
let tree = new BST();
tree.insert(66).insert(55).insert(99).insert(44).insert(60);
// console.log("INORDERARR")
console.log(tree.inorderArr(tree.root))
// console.log(tree.isEmpty())
// console.log(tree.getMin())
// console.log(tree.recursiveGetMin(tree.root))
console.log(tree.getMax())
// console.log(tree.recursiveGetMax(tree.root))
tree.deleteMin()
// console.log(tree.inorderArr(tree.root))
tree.deleteMax()
console.log(tree.inorderArr(tree.root))