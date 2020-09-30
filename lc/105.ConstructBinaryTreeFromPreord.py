# 105. Construct Binary Tree from Preorder and Inorder Traversal
# Medium

# 3935

# 104

# Add to List

# Share
# Given preorder and inorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# This approach does not work : 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
#         def helper(i):
#             if i > len(preorder)-1:
#                 return None
#             new_node = TreeNode(preorder[i])
#             new_node.left = helper(i+1)
#             new_node.right = helper(i+2)
#             return new_node
#         return helper(0)
        
        
        
        
# This solution works !!


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.idx_dict = {num: i for i, num in enumerate(inorder)}
        self.pre_cur_idx = 0
        
        def helper(in_start_idx, in_end_idx):
            if in_end_idx < in_start_idx:
                return None

            pre_cur_val = preorder[self.pre_cur_idx]
            self.pre_cur_idx += 1
            node = TreeNode(pre_cur_val)
            in_loc = self.idx_dict[pre_cur_val]
            node.left = helper(in_start_idx, in_loc - 1)
            node.right = helper(in_loc + 1, in_end_idx)
            return node
        
        return helper(0, len(inorder) - 1)
    
'''
inorder: left root right
preorder: root left right

we keep moving the index for pre order and for inorder, we find the index of the value in preorder arr at inorder arr and
its left is the left subtree and its right is the right subtree  

base case:             

if in_end_idx < in_start_idx:
                return None
'''