// const BSTinsert=(current, val)=>{

//     if(current === null){
//         return new BinaryNode(val)
//     }
//     else if(current.val<val){
//         if(current.right){
//             return BSTinsert(current.right, val)
//         }
//         else{
//             current.right = new BinaryNode(val)
//             return current.right
//         }
//     }
//     else if(current.val>val){
//         if (current.left){
//             return BSTinsert(current.left, val)
//         }
//         else{
//             current.left= new BinaryNode(val)
//             return current.left
//         }
//     }
// };

// class BinaryNode {
//     constructor(val){
//       this.val = val;
//       this.left = null;
//       this.right = null;
//     }
//   }
//   class BST {
//     constructor(node){
//       this.root = node;
//     }
//     insert(current, val){
//         return BSTinsert(current, val)
//     }
//   }

// console.log('here')
// let tree = new BST(new BinaryNode(77))
// console.log(tree)
// tree.insert(tree.root, 78)
// console.log(tree)
// tree.insert(tree.root, 60)
// console.log(tree)
// tree.insert(tree.root, 90)
// console.log(tree)
// tree.insert(tree.root, 100)
// console.log(tree)
// tree.insert(tree.root, 30)
// console.log(tree)
// tree.insert(tree.root, 65)
// console.log(tree)
// tree.insert(tree.root, 75)
// console.log(tree)
// tree.insert(tree.root, 80)
// console.log(tree)
// tree.insert(tree.root, 76)
// console.log(tree)

  // console.log(BTSinsert())
  // given a root node 'current' and a new node value 'val',
  // insert that node into a BST.
  // create a stand alone function or attach a new method to the BST class.

  class BinaryNode {
    constructor(val){
      this.val = val;
      this.left = null;
      this.right = null;
    }
  }
  class BST {
    constructor(){
      this.root = null;
    }
    insert(val, current){
      if(this.root == null){
        this.root = new BinaryNode(val);
        return this;
      }
      if(!current){
        current = this.root;
      }
      if(val > current.val && current.right != null){
        this.insert(val, current.right);
      }
      if(val > current.val && current.right == null){
        current.right = new BinaryNode(val);
      }
      if(val < current.val && current.left != null){
        this.insert(val, current.left);
      }
      if(val < current.val && current.left == null){
        current.left = new BinaryNode(val);
      }
      return this;
    }
  }
  let tree = new BST();
  tree.insert(66).insert(55).insert(99).insert(44).insert(60);
  console.log(tree.root.left.left);

