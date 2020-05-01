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
    getMin(runner=this.root){

        if(!runner){
            return null;
        }

        while(runner.left){
            runner = runner.left;
        }

        return runner.val;
    }

    getMax(runner=this.root){

        if(!runner){
            return null;
        }

        while(runner.right){
            runner = runner.right;
        }

        return runner.val;
    }

    // recursiveGetMin(node){
    //     if(!node) node = this.root;

    //     if(!node.left) return node.val;

    //     return this.recursiveGetMin(node.left);
    // }


    // recursiveGetMax(node){
    //     if(!node) node = this.root;

    //     if(!node.right) return node.val;

    //     return this.recursiveGetMax(node.right);
    // }
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
    delete(value){  
        var current = null;
        var runner = this.root;
        if (runner === null){
            return;
        }
        while(runner){
            if (runner.val === value){
                if(runner.left === null && runner.right === null){
                    if (current === null) {
                        this.root = null
                    } else {
                        if (current.left === runner) {
                            current.left = null
                        } else {
                            current.right = null
                        }
                    }
                }
        
                else if( runner.right==null){
                    let max = this.getMax(runner.left);
                    runner.val =max;
                    runner.left = this.deleteMax(runner.left)
                }
                else {
                    let min = this.getMin(runner.right);
                    runner.val =min;
                    runner.right = this.deleteMin(runner.right)
                }
                return this;
            }
            else if(runner.val < value){
                current = runner;
                runner = runner.right;

            }
            else if (runner.val > value){
                current = runner;
                runner = runner.left
                }
            }
        return this;
        }

    deleteMax(current=this.root){
        let originalHead = current
        if (current===null){
            return null}
        if (current.right === null) {
            return current.left
        }
        let next =current.right;
        while (next.right !== null){
            current = next;
            next = next.right;
        }
        current.right = next.left;
        return originalHead;
    }
    deleteMin(current=this.root){
        let originalHead = current
        if (current===null){
            return null}
        if (current.left === null) {
            return current.right
        }
        let next =current.left;

        while (next.left !== null){
            current = next;
            next = next.left;
        }
        current.left = next.right;
        return originalHead;
    }
    // remove(target){
    //   this.root = this.recursiveRemove(this.root, target);
    // }
    // recursiveRemove(current, target){
    //   // if root is null return empty
    //   if(current === null){ 
    //     return null;
    //   // if less than current go left
    //   }else if(target < current.val){
    //     current.left = this.recursiveRemove(current.left, target);
    //     return current;
    //   // if more go right
    //   }else if(target > current.val){
    //     current.right = this.recursiveRemove(current.right, target);
    //     return current;
    //   // hey we found it, let's delete
    //   }else{
    //     // no children
    //     if(current.left === null && current.right === null){
    //       current = null;
    //       return current;
    //     }
    //     // right children
    //     if(current.left === null){
    //       current = current.right;
    //       return current;
    //     }
    //     // left children
    //     else if(current.right === null){
    //       current = current.left;
    //       return current
    //     }
    //     // two children, find the min of the right tree
    //     let min = this.getMin(current.right);
    //     current.val = min;
    //     // and now remove that min value instead
    //     current.right = this.recursiveRemove(current.right, min);
    //     return current;
    //   }
    // }
    // height(){ 
    //   if(this.root == null){
    //     return 0;
    //   }
    //   return this.rheight(this.root);
    // }
    // rheight(current){
    //     if(current == null){
    //       return 0;
    //     }
    //     let leftTree = this.rheight(current.left);
    //     let rightTree = this.rheight(current.right);
    //     if(leftTree >= rightTree){
    //       return leftTree + 1;
    //     }else{
    //       return rightTree +1;
    //     }
    // }
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
  tree.delete(44)
//   tree.delete(66)
//   tree.delete(99)
  tree.delete(50)
//   tree.delete(55)
//   tree.delete(101)
//   tree.delete(62)
//   tree.delete(75)
  InorderTraversal(tree.root);
  
  

  
  