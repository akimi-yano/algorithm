# 1382. Balance a Binary Search Tree

# Given a binary search tree, return a balanced binary search tree with the same node values.

# A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

# If there is more than one answer, return any of them.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# This does not work - think why
# class Solution:
#     def balanceBST(self, root: TreeNode) -> TreeNode:

#         def balanced(cur):
#             if cur is None:
#                 return 0
#             left = balanced(cur.left)
#             right = balanced(cur.right)
            
#             if abs(left - right)>1:
#                 return (1+left+right)*(-1)
#             else:
#                 return 1+left+right
        
#         is_balanced = balanced(root)
#         if is_balanced>0:
#             return root
#         else:
#             count = is_balanced*(-1)
#             half = (count-1)//2
#             for _ in range(half):
#                 root = root.
                
                
# Below works - 
# this is cool
# do inorder traversal to make a sorted list of BST and then build a balanced tree doing binary search ! 
# start from the middle as a root 

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        nodes = []
        
        def in_order_traverse(root):
            if root is None:return
            in_order_traverse(root.left)
            nodes.append(root)
            in_order_traverse(root.right)
        
        def build_balanced_tree(left, right):
            if left>right:return None
            mid = (left+right)//2
            root = nodes[mid]
            root.left = build_balanced_tree(left, mid-1)
            root.right = build_balanced_tree(mid+1, right)
            return root
        in_order_traverse(root)
        return build_balanced_tree(0, len(nodes)-1)