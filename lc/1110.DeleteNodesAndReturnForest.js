// 1110. Delete Nodes And Return Forest
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
 * @param {number[]} to_delete
 * @return {TreeNode[]}
 */
var delNodes = function(root, to_delete) {
    let result = []
    let toDel = new Set(to_delete)
    
    function remove(node){
        if(node == null){
            return null
        }
        node.left = remove(node.left)
        node.right= remove(node.right)
        
        if(toDel.has(node.val)){
            if(node.left){
                result.push(node.left)
            }
            if(node.right){
                result.push(node.right)
            }
            return null
        }
        
        return node
        
    }
    remove(root)
    
    if(!toDel.has(root.val)){
        result.push(root)
    }
    return result
};