# 814. Binary Tree Pruning
# Medium

# 2683

# 77

# Add to List

# Share
# Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

# A subtree of a node node is node plus every node that is a descendant of node.

 

# Example 1:


# Input: root = [1,null,0,0,1]
# Output: [1,null,0,null,1]
# Explanation: 
# Only the red nodes satisfy the property "every subtree not containing a 1".
# The diagram on the right represents the answer.
# Example 2:


# Input: root = [1,0,1,0,0,0,1]
# Output: [1,null,1,null,1]
# Example 3:


# Input: root = [1,1,0,1,1,0,1,0]
# Output: [1,1,0,1,1,null,1]
 

# Constraints:

# The number of nodes in the tree is in the range [1, 200].
# Node.val is either 0 or 1.


# This solution works:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        '''
        (1)
        
        
        (0)
        
        (1) (1) / (0) (1) / (1) (0) / (0) (0)
        
        '''
        
        def helper(cur):
            if not cur:
                return False
            left = helper(cur.left)
            right = helper(cur.right)
            if not left:
                cur.left = None
            if not right:
                cur.right = None
            return left or right or cur.val
        
        if not helper(root):
            return None
        return root
        