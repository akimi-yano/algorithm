// BST Delete
// does the node have one or more children?
// is the node the root node?
// is the node a leaf node with no children?
// which node do we need access to, in order to delete 37?
// BST Get Smallest
// BST Get Largest
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
    getMin(current){
      if(!current){
        current = this.root;
      }
      while(current.left !== null){
        current = current.left;
      }
      return current.val;
    }
    while(runner){
      if (runner.val === value){
          if(runner.left === null && runner.right === null){
              runner = null;
          }
          // else if(runner.left  === null){
          //     runner=runner.right;

          // }
          // else if (runner.right === null){
          //     runner=left
          // }
          else if( runner.right==null){
              let max = this.getMax(runner.left);
              runner.val =max;
              this.deleteMax(runner.left)
          }
          else if(runner.left!== null && runner.right!==null || runner.left === null){
              let min = this.recursiveGetMin(runner.right);
              runner.val =min;
              this.deleteMin(runner.right)
          }
      }
      else if(runner.val < value){
          runner2 = runner; //make it equal to runner before we move
          runner = runner.right;

      }
      else if (runner.val > value){
          runner2 = runner;
          runner = runner.left
          }
      }
  return this;
  }
    remove(target){
      // call remove on the root node
      this.root = this.recursiveRemove(this.root, target);
    }
    recursiveRemove(current, target){
      // if root is null return empty
      if(current === null){ 
        return null;
      // if less than current go left
      }else if(target < current.val){
        current.left = this.recursiveRemove(current.left, target);
        return current;
      // if more go right
      }else if(target > current.val){
        current.right = this.recursiveRemove(current.right, target);
        return current;
      // hey we found it, let's delete
      }else{
        // no children
        if(current.left === null && current.right === null){
          current = null;
          return current;
        }
        // right children
        if(current.left === null){
          current = current.right;
          return current;
        }
        // left children
        else if(current.right === null){
          current = current.left;
          return current
        }
        // two children, find the min of the right tree
        let min = this.getMin(current.right);
        current.val = min;
        // and now remove that min value instead
        current.right = this.recursiveRemove(current.right, min);
        return current;
      }
    }
    height(){ 
      if(this.root == null){
        return 0;
      }
      return this.rheight(this.root);
    }
    rheight(current){
        if(current == null){
          return 0;
        }
        let leftTree = this.rheight(current.left);
        let rightTree = this.rheight(current.right);
        if(leftTree >= rightTree){
          return leftTree + 1;
        }else{
          return rightTree +1;
        }
    }
  }
  function InorderTraversal(current){
    if(current == null){
      return;
    }
    
    InorderTraversal(current.left);
    console.log(current.val);
    InorderTraversal(current.right);
  }
  let tree = new BST();
  tree.insert(66).insert(55).insert(99).insert(44).insert(50).insert(101).insert(62).insert(75);
  // console.log(tree.height());
  // InorderTraversal(tree.root);
  tree.remove(44);
  // console.log(tree.height());
  InorderTraversal(tree.root);
  
  

  
  