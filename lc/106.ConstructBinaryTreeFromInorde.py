# 106. Construct Binary Tree from Inorder and Postorder Traversal
# Medium

# 1801

# 37

# Add to List

# Share
# Given inorder and postorder traversal of a tree, construct the binary tree.

# Note:
# You may assume that duplicates do not exist in the tree.

# For example, given

# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
# Return the following binary tree:

#     3
#    / \
#   9  20
#     /  \
#    15   7


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # inorder: left root right -> use this to find a left and right
        # postorder: left right root -> use this to find a root
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        # find index of the root from inorder arr
        root_idx = inorder.index(root.val)
        
        # start with right to left
        # That's because inorder traversal goes 'Left-Parent-Right' and postorder traversal goes 
        # 'Left-Right-Parent'. And, postorder.pop() keeps picking the right-most element of the list, 
        # that means it should go 'Parent-(one of parents of) Right (subtree) - Left'. 
        # So, switching the order doesn't work.
        root.right = self.buildTree(inorder[root_idx+1:],postorder)
        root.left = self.buildTree(inorder[:root_idx],postorder)
        
        return root