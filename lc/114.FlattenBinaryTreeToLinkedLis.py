# 114. Flatten Binary Tree to Linked List
# Medium

# 3927

# 391

# Add to List

# Share
# Given the root of a binary tree, flatten the tree into a "linked list":

# The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
# The "linked list" should be in the same order as a pre-order traversal of the binary tree.
 

# Example 1:


# Input: root = [1,2,5,3,4,null,6]
# Output: [1,null,2,null,3,null,4,null,5,null,6]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 2000].
# -100 <= Node.val <= 100
 

# Follow up: Can you flatten the tree in-place (with O(1) extra space)?


# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(cur):
            if not cur:
                return
            nonlocal arr
            arr.append(cur)
            helper(cur.left)
            helper(cur.right)
        
        arr = []
        helper(root)
        
        for i, node in enumerate(arr):
            node.right = arr[i+1] if i+1 < len(arr) else None
            node.left = None
        return root
    
    
# This solution works - constant space:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.right:
                if cur.left is None:
                    cur = cur.right
                    continue

                left_rightmost = cur.left
                while left_rightmost.right is not None:
                    left_rightmost = left_rightmost.right
                left_rightmost.right = cur.right
                cur.right = cur.left
                cur.left = None
                cur = cur.right
            else:
                cur.right = cur.left
                cur.left = None
                cur = cur.right
        return root