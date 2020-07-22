// 230. Kth Smallest Element in a BST
// Given a binary search tree, write a function kthSmallest to 
// find the kth smallest element in it.
 
// Example 1:

// Input: root = [3,1,4,null,2], k = 1
//    3
//   / \
//  1   4
//   \
//    2
// Output: 1
// Example 2:

/**
left
operation
right
//        3
//      /  \
//    1     4
//     \
//     2
// Output

  k
//1, 2, 3, 4
Inorder List Runtime O(n) + Stack recursion,  memory O(n)


**/
// Input: root = [5,3,6,2,4,null,null,1], k = 3
//        5
//       / \
//      3   6
//     / \
//    2   4
//   /
//  1
// Output: 3


// Follow up:
// What if the BST is modified (insert/delete operations) often and you 
// need to find the kth smallest frequently? How would you optimize the 
// kthSmallest routine?

 

// Constraints:

// The number of elements of the BST is between 1 to 10^4.
// You may assume k is always valid, 1 ≤ k ≤ BST's total elements.


public class TreeNode {
    int val;
     TreeNode left;
     TreeNode right;
     TreeNode() {}
     TreeNode(int val) { this.val = val; }
     TreeNode(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }

//https://leetcode.com/problems/kth-smallest-element-in-a-bst/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
  
  /**
  left
operation
right
  **/
    public int kthSmallest(TreeNode root, int k) {
          if(k == 0){
            return 0;
          }
          if(root == null){
            return -1;
          }
          inOrder(root);
          return inOrderTree.get(k-1);
    }
    
    List<TreeNode> inOrderTree = new Arraylist<>();
    
    public void inOrder(TreeNode root){
      if(root == null){
        return;
      }
      
      inOrder(root.left);
      inOrderTree.add(root);
      inOrder(root.right);
    }
    
     public int kthSmallest2(TreeNode root, int k) {
          if(k == 0){
            return 0;
          }
          if(root == null){
            return -1;
          }
          return inOrder2(0, root, k);
    }
    
    public int inOrder2(int count, TreeNode root, int k){
      if(root == null){
        return 0;
      }
      
      return inOrder2(count+1, root.left);
      if(count++ == k){
        return root.val;
      }
      return inOrder2(count+1, root.right);
    }
    
    
    
}


/// different problem 


public Node getNode(Node root, int k) {
		if(root == null){
			return null; // This case means k > tree size
		} 
		int left = root.left == null ? 0 : root.left.countDescendants;

		if(left >= k){
			return getNode(root.left, k);
		} 
		else if(left + 1 == k){
			return root;
		} 
		else{
			return getNode(root.right, k-left-1);
		} 
	}public int value;
  public int countDescendants;
  public Node left;
  public Node right;