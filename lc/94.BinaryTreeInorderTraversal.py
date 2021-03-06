# 94. Binary Tree Inorder Traversal
# Medium

# 4353

# 192

# Add to List

# Share
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [1,3,2]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
# Example 4:


# Input: root = [1,2]
# Output: [2,1]
# Example 5:


# Input: root = [1,null,2]
# Output: [1,2]
 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 

# Follow up:

# Recursive solution is trivial, could you do it iteratively?

# This solution works:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        def helper(cur):
            if not cur:
                return
            nonlocal arr
            helper(cur.left)
            arr.append(cur.val)
            helper(cur.right)
        
        arr = []
        helper(root)
        return arr
    
    
# This solution works - iterative:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        stack = [(root, False)]
        ans = []
        while stack:
            node, traversed = stack.pop()
            if not node:
                continue
            if not traversed:
                stack.append((node.right, False))
                stack.append((node, True))
                stack.append((node.left, False))
            else:
                ans.append(node.val)
        return ans