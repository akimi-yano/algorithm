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
        