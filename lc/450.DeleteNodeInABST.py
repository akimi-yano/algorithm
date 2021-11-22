# 450. Delete Node in a BST
# Medium

# 4105

# 129

# Add to List

# Share
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.
 

# Example 1:


# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:

# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.
# Example 3:

# Input: root = [], key = 0
# Output: []
 

# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -105 <= Node.val <= 105
# Each node has a unique value.
# root is a valid binary search tree.
# -105 <= key <= 105
 

# Follow up: Could you solve it with time complexity O(height of tree)?


# This solution works:


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


