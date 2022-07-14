# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

# 9258

# 254

# Add to List

# Share
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

 

# Example 1:


# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
# Example 2:

# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
 

# Constraints:

# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        '''
        Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
        Output: [3,9,20,null,null,15,7]
        
        p_idx 0 = 3 cur
        p_idx 1 = 9 left
        p_idx 2 = 20 right
        
        
        
        '''
        def helper(start, end):
            nonlocal p_idx
            if end < start:
                return None
        
            cur = TreeNode(preorder[p_idx])
            par_loc = inorder.index(preorder[p_idx])
            p_idx += 1
            cur.left = helper(start, par_loc-1)
            cur.right = helper(par_loc+1, end)
            return cur
        p_idx = 0
        return helper(0, len(inorder)-1)
