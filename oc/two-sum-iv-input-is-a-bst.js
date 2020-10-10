/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {boolean}
 * 
 * https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
 * 
 * 
 */


var findTarget = function(root, k) {
  const visited = new Set();
  let flag = false;
  function traverse(curr) {
    if (curr === null) {
      return;
    }
    if (flag) {
      return;
    }

    let diff = k - curr.val;
    if (visited.has(diff)) {
      flag = true;
      return;
    }
    visited.add(curr.val);
    traverse(curr.left);
    traverse(curr.right);
  }
  traverse(root);

  return flag;
};