# 450. Delete Node in a BST

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
# Note: Time complexity should be O(height of tree).

# Example:

# root = [5,3,6,2,4,null,7]
# key = 3

#     5
#    / \
#   3   6
#  / \   \
# 2   4   7

# Given key to delete is 3. So we find the node with value 3 and delete it.

# One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

#     5
#    / \
#   4   6
#  /     \
# 2       7

# Another valid answer is [5,2,6,null,4,null,7].

#     5
#    / \
#   2   6
#    \   \
#     4   7






# THIS SOLUTION DOES NOT WORK :

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
#         '''
#         find the node
#         up date the min of the next node to it by returning the smaller noder
#         '''
#         self.key = key
#         def helper(cur):
#             found = False
#             if not cur:
#                 return 
#             if cur.val == self.key:
#                 found = True
#             cur.left = helper(cur.left)
#             cur.right = helper(cur.right)
            
#             if not found:
#                 return cur
#             elif found:
#                 if not cur.left and not cur.right:
#                     return
#                 elif not cur.left:  
#                     smaller = cur.right
#                     smaller.left = cur.left
#                 elif not cur.right:
#                     smaller = cur.left
#                     smaller.right = cur.right
#                 elif cur.left.val < cur.right.val:
#                     smaller = cur.left
#                     smaller.right = cur.right
#                 else:
#                     smaller = cur.right
#                     smaller.left = cur.left
#                 return smaller
#         return helper(root)


# THIS SOLUTION WORKS !!! and very intuitive !!! Gonna review more !!!

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        '''
        args: root(node), key(val to remove)
        1 find the key by doing BS
        2 if found - check how many children they have: 0, 1, or 2 ?
        3 if 0 ; if 1; if 2, get min from the right subtree ans copy its value and remove it 
        
        '''
        if not root:
            return root
        elif root.val>key:
            root.left = self.deleteNode(root.left, key)
        elif root.val<key:
            root.right = self.deleteNode(root.right, key)
        # found the val
        else:
            # no child
            if not root.left and not root.right:
                root = None
            # 1 child 
            elif not root.right:
                root = root.left
            elif not root.left:
                root = root.right
            # 2 children
            else:
                temp_node = self.find_min_from_right_subtree(root.right)
                root.val = temp_node.val
                root.right = self.deleteNode(root.right,temp_node.val)
        return root
            
    def find_min_from_right_subtree(self, cur):
        # to find min, keep going left
        while cur.left:
            cur = cur.left
        return cur