# 897. Increasing Order Search Tree
# Easy

# 921

# 492

# Add to List

# Share
# Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.

 

# Example 1:


# Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# Example 2:


# Input: root = [5,1,7]
# Output: [1,null,5,null,7]
 

# Constraints:

# The number of nodes in the given tree will be in the range [1, 100].
# 0 <= Node.val <= 1000


# This approach works !

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def helper(cur):
            if not cur:
                return None
            helper(cur.left)
            ans.append(cur)
            helper(cur.right)
        ans = []
        helper(root)
        for i in range(len(ans)):
            ans[i].left = None
            ans[i].right = None
        root = ans[0]
        cur = root
        for i in range(1, len(ans)):
            cur.right = ans[i]
            cur = cur.right
        return root
            
            
# This solution works 
'''
dfs inorder traversal - passing cur and prev 
the prev.right is cur
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.helper(root, None)
        return self.head
    
    def helper(self, cur, prev):
        if cur is None:
            return prev
        
        # left
        new_prev = self.helper(cur.left, prev)

        cur.left = None
        
        # yourself
        if new_prev is None:
            self.head = cur
        else:
            new_prev.right = cur
            
        # right
        return self.helper(cur.right, cur)