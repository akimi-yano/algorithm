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

    count(current){
        if(current ==null){
            return 0
        }
        let leftCount = this.count(current.left)
        let rightCount = this.count(current.right)
        let myCount = 1
        return leftCount + rightCount + myCount
    }
    height(current){
        if(current ==null){
            return 0
        }
        let leftHeight = this.height(current.left)
        let rightHeight = this.height(current.right)
        let myHeight = 1
        if (leftHeight >= rightHeight){
            return leftHeight + myHeight
        }
        else if(rightHeight > leftHeight){
            return rightHeight + myHeight
        }
    }

}
let tree = new BST();
tree.insert(66).insert(55).insert(99).insert(44).insert(60)
// tree.insert(66).insert(55).insert(99).insert(44).insert(60).insert(61).insert(100)
// console.log(tree.root.left.left);
console.log(tree)
console.log(tree.count(tree.root))
console.log(tree.height(tree.root))